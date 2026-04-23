#!/usr/bin/env python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)
sns.set_style("whitegrid")

# Загрузка данных
df = pd.read_csv("mental_health_risk_dataset.csv")

# =====================================================================
# Тепловая карта 1: Корреляция всех числовых признаков
# =====================================================================
plt.figure(figsize=(14, 10))
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",
            linewidths=0.5, square=True, cbar_kws={"shrink": 0.8})
plt.title('Корреляционная матрица всех числовых признаков', fontsize=16)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'heatmap_all_numeric.png'))
plt.close()

# =====================================================================
# Тепловая карта 2: Только психологические показатели
# =====================================================================
psych_vars = ['anxiety_score', 'depression_score', 'stress_level', 'mood_swings_frequency']
psych_labels = ['Тревожность', 'Депрессия', 'Стресс', 'Перепады настроения']
df_psych = df[psych_vars].copy()
df_psych.columns = psych_labels

plt.figure(figsize=(8, 6))
sns.heatmap(df_psych.corr(), annot=True, fmt=".2f", cmap="YlOrRd",
            linewidths=0.5, square=True, cbar_kws={"shrink": 0.8})
plt.title('Корреляционная матрица психологических показателей', fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'heatmap_psych.png'))
plt.close()
