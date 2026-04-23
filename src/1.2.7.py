#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import os

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv("mental_health_risk_dataset.csv")

# ================================================================
# Ящик с усами для уровня финансового стресса
# ================================================================
plt.figure(figsize=(6, 4))
plt.boxplot(df['financial_stress_level'], vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue'))
plt.title('Ящик с усами: финансовый стресс', fontsize=14)
plt.ylabel('Уровень финансового стресса', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'boxplot_financial_stress.png'))
plt.close()

# ================================================================
# Определение выбросов методом IQR
# ================================================================
Q1 = df['financial_stress_level'].quantile(0.25)
Q3 = df['financial_stress_level'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['financial_stress_level'] < lower_bound) |
              (df['financial_stress_level'] > upper_bound)]

print(f"Нижняя граница: {lower_bound:.2f}, Верхняя граница: {upper_bound:.2f}")
print(f"Количество выбросов: {len(outliers)}")

df_clean = df[(df['financial_stress_level'] >= lower_bound) &
              (df['financial_stress_level'] <= upper_bound)]
