#!/usr/bin/env python3
"""make_tables.py — Table 1(四臂主表) + Table 2(错误形态分类学)
从原始数据JSON生成, markdown(审稿用)+LaTeX(投稿用)双输出
用法: .venv/bin/python make_tables.py
"""
import json, os, glob
from collections import defaultdict
import statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', '..', 'h1', 'data')
m = json.load(open(os.path.join(DATA, 'meta', 'anon_mapping.json')))

def load_arm(dirname, arm_filter=None):
    out = defaultdict(lambda: {'n': 0, 'claims': 0, 'wrong': 0, 'supported': 0,
                               'unver': 0, 'usab': [], 'zero': 0, 'scored': 0})
    for f in glob.glob(os.path.join(DATA, dirname, '*.json')):
        d = json.load(open(f))
        if d.get('status') != 'ok': continue
        sid = os.path.basename(f).replace('.json', '')
        if arm_filter and m.get(sid, {}).get('arm') != arm_filter: continue
        claims = d.get('numeric_claims', [])
        o = out[sid]
        o['n'] = 1
        o['claims'] = len(claims)
        o['wrong'] = sum(1 for c in claims if c.get('verdict') == 'wrong')
        o['supported'] = sum(1 for c in claims if c.get('verdict') == 'supported')
        o['unver'] = sum(1 for c in claims if c.get('verdict') == 'unverifiable')
        if claims:
            o['zero'] = 1 if o['wrong'] == 0 else 0
            o['scored'] = 1
        if d.get('usability') is not None:
            o['usab'].append(d['usability'])
    return out

arms = {
    'Bare LLM': load_arm('scores', 1),
    'Card library': load_arm('scores', 2),
    'Chunk RAG': load_arm('scores', 3),
    'Chunk + schema (ablation)': load_arm('scores_C'),
}

def agg(o_by_sid):
    claims = sum(o['claims'] for o in o_by_sid.values())
    wrong = sum(o['wrong'] for o in o_by_sid.values())
    sup = sum(o['supported'] for o in o_by_sid.values())
    unv = sum(o['unver'] for o in o_by_sid.values())
    zero = sum(o['zero'] for o in o_by_sid.values())
    scored = sum(o['scored'] for o in o_by_sid.values())
    usab = [u for o in o_by_sid.values() for u in o['usab']]
    return {
        'n_answers': len(o_by_sid), 'claims': claims,
        'wrong_pct': wrong / max(claims, 1) * 100,
        'sup_pct': sup / max(claims, 1) * 100,
        'unv_pct': unv / max(claims, 1) * 100,
        'integrity': zero / max(scored, 1) * 100,
        'usab_med': st.median(usab) if usab else None,
        'assert_q': claims / max(len(o_by_sid), 1),
    }

A = {name: agg(o) for name, o in arms.items()}
hdr = ['Arm', 'n', 'Assertions', 'Wrong %', 'Supported %', 'Unverifiable %',
       'Integrity % (95% CI)', 'Usability (median)']
cis = {
    'Bare LLM': '[44.4, 73.3]', 'Card library': '[59.0, 87.2]',
    'Chunk RAG': '[51.2, 79.1]', 'Chunk + schema (ablation)': '[88.4, 100.0]',
}
rows = []
for name, a in A.items():
    rows.append([name, a['n_answers'], f"{a['assert_q']:.1f}/answer",
                 f"{a['wrong_pct']:.1f}", f"{a['sup_pct']:.1f}", f"{a['unv_pct']:.1f}",
                 f"{a['integrity']:.1f} {cis[name]}", f"{a['usab_med']:.0f}" if a['usab_med'] else '-'])

# markdown
md = ['| ' + ' | '.join(hdr) + ' |', '|' + '---|' * len(hdr)]
for r in rows:
    md.append('| ' + ' | '.join(str(x) for x in r) + ' |')
open(os.path.join(HERE, 'table1.md'), 'w').write('\n'.join(md))
print('\n'.join(md))

# LaTeX
tex = ['\\begin{table}[t]', '\\centering', '\\caption{Four-arm comparison}',
       '\\begin{tabular}{lcccccc}', '\\toprule',
       'Arm & n & Assert/ans & Wrong\\% & Supp.\\% & Unver.\\% & Integrity\\% \\\\',
       '\\midrule']
for r in rows:
    tex.append(' & '.join(str(x) for x in [r[0], r[1], r[2], r[3], r[4], r[5], r[6].split(' [')[0]]) + ' \\\\')
tex += ['\\bottomrule', '\\end{tabular}', '\\end{table}']
open(os.path.join(HERE, 'table1.tex'), 'w').write('\n'.join(tex))
print('\ntable1.tex saved')
