#!/usr/bin/env python3
"""fig3_pipeline.py — Figure 3: 发现驱动的改进闭环(P2 A/B + 完整链路)
四指标前后对比: supported 59.3→82.7 / unverifiable 39→15.9 / wrong 1.6→1.4 / 完整链路零错误97.4%
数据源: ab_p2_results.json + 生产链路实测
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.9), dpi=300)
metrics = [
    ('Supported rate (%)', 59.3, 82.7, '+23.4 pp', '#0f7b6c'),
    ('Unverifiable (%)',   39.0, 15.9, '-23.1 pp', '#4a53b8'),
    ('Wrong rate (%)',      1.6,  1.4, 'NS (no regression)', '#b3591f'),
]
for ax, (label, v1, v2, delta, c) in zip(axes, metrics):
    bars = ax.bar(['v1', 'v2'], [v1, v2], color=['#bbbbbb', c], width=.62,
                  edgecolor='none')
    for b, v in zip(bars, (v1, v2)):
        ax.text(b.get_x() + b.get_width()/2, v + 1.2, f'{v:.1f}', ha='center',
                fontsize=10, fontweight='bold')
    ax.set_title(f'{label}\n{delta}', fontsize=9.5)
    ax.set_ylim(0, max(v1, v2) * 1.28)
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(labelsize=9)
fig.suptitle('Same 39 questions, same scorer: generation-prompt v1 → v2 (source-anchored citation discipline)',
             fontsize=9.5, y=1.04)
fig.tight_layout()
fig.savefig('fig3_pipeline.pdf', bbox_inches='tight')
fig.savefig('fig3_pipeline.png', dpi=300, bbox_inches='tight')
print('fig3 saved')
