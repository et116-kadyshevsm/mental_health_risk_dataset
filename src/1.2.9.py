#!/usr/bin/env python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv("mental_health_risk_dataset.csv")

# Для воспроизводимости зафиксируем генератор случайных чисел
np.random.seed(42)

# Сохраним копию до добавления шума для сравнения
df_before_noise = df.copy()

# Добавим небольшой гауссов шум к двум признакам: sleep_hours и financial_stress_level
noise_std_sleep = 0.2
noise_std_fin = 0.3

df['sleep_hours'] = df['sleep_hours'] + np.random.normal(0, noise_std_sleep, size=len(df))
df['financial_stress_level'] = df['financial_stress_level'] + np.random.normal(0, noise_std_fin, size=len(df))

# Ограничим реалистичные диапазоны, чтобы не было отрицательных значений
df['sleep_hours'] = df['sleep_hours'].clip(lower=0)
df['financial_stress_level'] = df['financial_stress_level'].clip(lower=1, upper=10)

# Сравнение распределений до и после для одного из признаков (сон)
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.hist(df_before_noise['sleep_hours'], bins=20, alpha=0.7, label='До шума')
plt.hist(df['sleep_hours'], bins=20, alpha=0.7, label='После шума')
plt.title('Сон: распределение до и после шума')
plt.xlabel('Часы сна')
plt.ylabel('Частота')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'noise_sleep_compare.png'))
plt.close()
