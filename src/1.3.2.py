#!/usr/bin/env python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)
sns.set_style("whitegrid")

df = pd.read_csv("mental_health_risk_dataset.csv")

gender_map = {'Male': 'Мужчина', 'Female': 'Женщина', 'Other': 'Другой'}
marital_map = {'Single': 'Холост / не замужем', 'Married': 'В браке', 'Divorced': 'Разведён(а)'}
education_map = {'High School': 'Среднее', 'Bachelor': 'Бакалавр', 'Master': 'Магистр', 'PhD': 'Доктор'}
employment_map = {'Employed': 'Работает', 'Unemployed': 'Безработный', 
                  'Self-Employed': 'Самозанятый', 'Student': 'Студент'}

df['gender_ru'] = df['gender'].map(gender_map)
df['marital_status_ru'] = df['marital_status'].map(marital_map)
df['education_level_ru'] = df['education_level'].map(education_map)
df['employment_status_ru'] = df['employment_status'].map(employment_map)

categorical_cols_ru = ['gender_ru', 'marital_status_ru', 'education_level_ru', 'employment_status_ru']
titles = ['Пол', 'Семейное положение', 'Уровень образования', 'Статус занятости']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for ax, col, title in zip(axes, categorical_cols_ru, titles):
    order = sorted(df[col].unique())
    sns.countplot(data=df, x=col, ax=ax, palette='Set2', order=order)
    ax.set_title(f'Распределение по: {title}', fontsize=14)
    ax.set_xlabel('')
    ax.set_ylabel('Количество', fontsize=12)
    ax.tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'categorical_distributions.png'))
plt.close()
