#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import os

# Создание папки
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# Загрузка данных
df = pd.read_csv("mental_health_risk_dataset.csv")

# ============================================================
# График 1: Гистограмма распределения возраста
# ============================================================
plt.figure(figsize=(8, 5))
plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black', alpha=0.8)
plt.title('Распределение возраста респондентов', fontsize=14)
plt.xlabel('Возраст', fontsize=12)
plt.ylabel('Количество', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'pyplot_age_histogram.png'))
plt.close()

# ============================================================
# График 2: Ящик с усами – финансовый стресс по семейному положению
# ============================================================
marital_map = {'Single': 'Холост / не замужем',
               'Married': 'В браке',
               'Divorced': 'Разведён(а)'}
df['marital_status_ru'] = df['marital_status'].map(marital_map)
marital_order_ru = ['Холост / не замужем', 'В браке', 'Разведён(а)']

data_to_plot = [df[df['marital_status_ru'] == status]['financial_stress_level']
                for status in marital_order_ru]

plt.figure(figsize=(10, 6))
plt.boxplot(data_to_plot, labels=marital_order_ru, patch_artist=True,
            boxprops=dict(facecolor='lightgreen', color='darkgreen'),
            medianprops=dict(color='red'))
plt.title('Финансовый стресс в зависимости от семейного положения', fontsize=14)
plt.xlabel('Семейное положение', fontsize=12)
plt.ylabel('Уровень финансового стресса', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'pyplot_financial_stress_boxplot.png'))
plt.close()
