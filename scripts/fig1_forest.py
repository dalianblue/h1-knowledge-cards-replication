#!/usr/bin/env python3
"""fig1_forest.py — Figure 1: 四臂per-answer零错误率森林图(bootstrap 95%CI)
数据源: ../h1/data/four_arm_final_stats.json (跑 analyze 脚本再生成, 此处内置定稿数值)
输出: fig1_forest.pdf + fig1_forest.png (300dpi, JAMIA单栏宽~3.3in/双栏~7in)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 定稿数据(paper/h1/data/four_arm_final_stats.json)
arms = [
    ('Bare LLM',            60.0, 44.4, 73.3),
    ('Chunk RAG',           65.1, 51.2, 79.1),
    ('Distilled cards',     74.4, 59.0, 87.2),
    ('Chunk + schema (ablation)', 95.3, 88.4, 100.0),
]
colors = ['#999999', '#4a53b8', '#0f7b6c', '#b3591f']

fig, ax = plt.subplots(figsize=(7.0, 3.2), dpi=300)
ys = np.arange(len(arms))[::-1]
for (name, m, lo, hi), y, c in zip(arms, ys, colors):
    ax.plot([lo, hi], [y, y], color=c, lw=2.2, solid_capstyle='round', alpha=.85)
    ax.plot([m, m], [y-.18, y+.18], color=c, lw=2.8)
    ax.scatter([m], [y], s=52, color=c, zorder=3)
    ax.annotate(f'{m:.1f}% [{lo:.1f}, {hi:.1f}]', (hi + 1.2, y),
                va='center', ha='left', fontsize=9.5, color=c)

ax.set_yticks(ys)
ax.set_yticklabels([a[0] for a in arms], fontsize=10.5)
ax.set_xlim(35, 108)
ax.set_xticks([40, 50, 60, 70, 80, 90, 100])
ax.set_xlabel('Per-answer integrity: answers with zero wrong assertions (%)', fontsize=10.5)
ax.axvline(95, color='#a12568', ls=':', lw=1.2, alpha=.7)
ax.annotate('95% clinical target', (95, len(arms)-0.42), fontsize=8.5, color='#a12568',
            ha='center', alpha=.9)
ax.spines[['top', 'right', 'left']].set_visible(False)
ax.tick_params(left=False)
ax.set_xlim(35, 112)  # 右侧留白防100.0标注裁切
# 图注内置(alt text 与 caption 一并给出, 投稿时复制)
CAPTION = (
    'Figure 1. Per-answer integrity across four arms. Error bars show bootstrap 95% CIs '
    '(2,000 resamples). Integrity = proportion of answers containing zero wrong numeric '
    'assertions. Dotted line marks the 95% clinical target. Chunk+schema (ablation) differs '
    'significantly from Distilled cards (Fisher exact p=0.011).\n'
    'Alt text: Horizontal forest plot of four bars showing per-answer integrity: Bare LLM '
    '60.0% (CI 44.4-73.3), Chunk RAG 65.1% (51.2-79.1), Distilled cards 74.4% (59.0-87.2), '
    'Chunk+schema ablation 95.3% (88.4-100.0); a dotted vertical line marks the 95% clinical '
    'target, which only the ablation arm reaches.')
open('fig1_caption.txt', 'w').write(CAPTION)
fig.tight_layout()
fig.savefig('fig1_forest.pdf')
fig.savefig('fig1_forest.png', dpi=300)
print('fig1 saved')
