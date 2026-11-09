#!/usr/bin/env python3
"""fig4_tradeoff.py — Figure 4: 安全-覆盖权衡图(错误率×断言数, 四臂定位)
数据源: four_arm_final_stats.json + h1_results_summary.json(断言数)
核心信息: 格式管安全(左下), 蒸馏管覆盖(右上), 理想系统=两者兼得
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

points = [
    ('Bare LLM',                 7.3, 11.3, '#999999'),
    ('Chunk RAG',                5.9, 10.0, '#4a53b8'),
    ('Card library',             1.6, 17.6, '#0f7b6c'),
    ('Chunk + schema',           0.5,  9.2, '#b3591f'),
]
fig, ax = plt.subplots(figsize=(5.6, 4.0), dpi=300)
for name, wr, ncl, c in points:
    ax.scatter(ncl, wr, s=140, color=c, zorder=3, edgecolor='white', linewidth=1.2)
    dx, dy = (0.15, 0.35)
    ha = 'left'
    if name == 'Card library':
        dx, dy, ha = -0.15, 0.42, 'right'
    ax.annotate(name, (ncl + dx, wr + dy), fontsize=10, ha=ha, color=c,
                fontweight='bold')
ax.set_ylim(-0.6, 9.8)
ax.annotate('', xy=(9.22, 0.82), xytext=(9.0, 8.1),
            arrowprops=dict(arrowstyle='->', color='#a12568', lw=1.3, ls='--'))
ax.text(8.35, 8.35, 'format-as-constraint:\nschema empty-shell suppresses\nfree generation', fontsize=8.4,
        color='#a12568', ha='left', va='bottom')
ax.annotate('', xy=(17.35, 1.42), xytext=(10.3, 0.6),
            arrowprops=dict(arrowstyle='->', color='#0f7b6c', lw=1.3, ls='--'))
ax.text(12.5, 0.12, 'distillation-as-coverage:\nmore supported assertions', fontsize=8.4,
        color='#0f7b6c', ha='left')
ax.set_xlabel('Mean numeric assertions per answer (coverage)', fontsize=10.5)
ax.set_ylabel('Numeric error rate (%)', fontsize=10.5)
ax.set_xlim(8, 19.5)
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig('fig4_tradeoff.pdf')
fig.savefig('fig4_tradeoff.png', dpi=300)
print('fig4 saved')
