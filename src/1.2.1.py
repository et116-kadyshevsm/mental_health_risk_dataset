#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import os

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv('mental_health_risk_dataset.csv')

numeric_cols_info = [
    ('age', 'Возраст'),
    ('sleep_hours', 'Часы сна'),
    ('physical_activity_hours_per_week', 'Физ. активность (ч/нед)'),
    ('screen_time_hours_per_day', 'Экранное время (ч/день)'),
    ('social_support_score', 'Социальная поддержка (балл)'),
    ('work_stress_level', 'Рабочий стресс (уровень)'),
    ('academic_pressure_level', 'Академическое давление (уровень)'),
    ('job_satisfaction_score', 'Удовлетворённость работой (балл)'),
    ('financial_stress_level', 'Финансовый стресс (уровень)'),
    ('working_hours_per_week', 'Рабочие часы в неделю'),
    ('anxiety_score', 'Тревожность (балл)'),
    ('depression_score', 'Депрессия (балл)'),
    ('stress_level', 'Стресс (уровень)'),
    ('mood_swings_frequency', 'Частота смены настроения'),
    ('concentration_difficulty_level', 'Сложность концентрации')
]

n = len(numeric_cols_info)
ncols = 3
nrows = (n + ncols - 1) // ncols

fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(18, 5 * nrows))
axes = axes.flatten()

for i, (col, ru_name) in enumerate(numeric_cols_info):
    axes[i].hist(df[col], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    axes[i].set_title(f'{ru_name}')
    axes[i].set_xlabel(ru_name)
    axes[i].set_ylabel('Частота')

    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

plt.tight_layout()
plt.savefig('plots/Распределения гистограм.png', dpi=150, bbox_inches='tight')
