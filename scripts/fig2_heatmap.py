#!/usr/bin/env python3
"""fig2_heatmap.py — Figure 2: 五知识层×三臂数值错误率热图
数据源: 直接从 paper/h1/data/ 重算(scores/*.json × anon_mapping × h1_sample_table)
用法: .venv/bin/python fig2_heatmap.py
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', '..', 'h1', 'data')

bank = json.load(open(os.path.join(HERE, '..', '..', 'h1_sample_table.json')))
m = json.load(open(os.path.join(DATA, 'meta', 'anon_mapping.json')))
slug2sid = defaultdict(list)
for sid, info in m.items():
    slug2sid[info['slug']].append(sid)

LAYER_EN = {
    'A_数值密集': 'A Numeric-dense',
    'B_机制解释': 'B Mechanistic\n(honesty control)',
    'C_临床决策': 'C Clinical decision',
    'D_指南推荐': 'D Guideline recommendation',
    'E_近期热点': 'E Recent / hot topic',
}
layer_stat = defaultdict(lambda: defaultdict(lambda: [0, 0]))
for layer, slugs in bank.items():
    if layer.startswith('_'): continue
    for slug in slugs:
        for sid in slug2sid.get(slug, []):
            arm = m[sid]['arm']
            if arm == 'C': continue
            sf = os.path.join(DATA, 'scores', f'{sid}.json')
            if not os.path.exists(sf): continue
            d = json.load(open(sf))
            if d.get('status') != 'ok': continue
            claims = d.get('numeric_claims', [])
            layer_stat[layer][arm][1] += len(claims)
            layer_stat[layer][arm][0] += sum(1 for c in claims if c.get('verdict') == 'wrong')

layers_cn = ['A_数值密集', 'B_机制解释', 'C_临床决策', 'D_指南推荐', 'E_近期热点']
data = np.array([[layer_stat[l][a][0] / max(layer_stat[l][a][1], 1) * 100
                  for a in (1, 2, 3)] for l in layers_cn])
counts = [[f'{layer_stat[l][a][0]}/{layer_stat[l][a][1]}' for a in (1, 2, 3)] for l in layers_cn]

arms = ['Bare LLM', 'Card library', 'Chunk RAG']
fig, ax = plt.subplots(figsize=(6.2, 3.8), dpi=300)
im = ax.imshow(data, cmap='RdYlGn_r', aspect='auto', vmin=0, vmax=16)
ax.set_xticks(range(3)); ax.set_xticklabels(arms, fontsize=10)
ax.set_yticks(range(5)); ax.set_yticklabels([LAYER_EN[l] for l in layers_cn], fontsize=9)
for i in range(5):
    for j in range(3):
        v = data[i, j]
        ax.text(j, i, f'{v:.1f}%\n({counts[i][j]})', ha='center', va='center',
                fontsize=8.6, color='white' if v > 10 else '#222',
                fontweight='bold' if (i == 4 and j == 2) else 'normal')
cb = fig.colorbar(im, ax=ax, shrink=.85)
cb.set_label('Numeric error rate (%)', fontsize=9.5)
ax.annotate('E layer: chunk RAG worse than bare LLM\n(recent knowledge fails without distillation)',
            xy=(2, 4), xytext=(0.30, -0.16), textcoords='axes fraction',
            fontsize=8.2, color='#a12532', ha='left')
fig.tight_layout()
fig.savefig('fig2_heatmap.pdf')
fig.savefig('fig2_heatmap.png', dpi=300)
print('fig2 saved (data recomputed from scores/)')

# 同步打印核实数字
for i, l in enumerate(layers_cn):
    print(l, [f'{data[i,j]:.1f}%' for j in range(3)])
