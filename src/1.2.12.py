#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv("mental_health_risk_dataset.csv")

df_before_noise = df.copy()

# Имитация добавления шума (повтор действия из пункта 1.2.9)
np.random.seed(42)
df['sleep_hours'] = df['sleep_hours'] + np.random.normal(0, 0.2, size=len(df))
df['sleep_hours'] = df['sleep_hours'].clip(lower=0)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(df['sleep_hours'], bins=20, edgecolor='black', alpha=0.8)
plt.title('Распределение часов сна (после шума)')
plt.xlabel('Часы сна')
plt.ylabel('Частота')

plt.subplot(1, 2, 2)
plt.hist(df['age'], bins=20, edgecolor='black', alpha=0.8)
plt.title('Распределение возраста (исходное)')
plt.xlabel('Возраст')
plt.ylabel('Частота')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'final_distributions.png'))
plt.close()

# Сравнение статистик до и после добавления шума
print("Статистика sleep_hours до шума:")
print(df_before_noise['sleep_hours'].describe())
print("\nСтатистика sleep_hours после шума:")
print(df['sleep_hours'].describe())
