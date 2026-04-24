#!/usr/bin/env python
import pandas as pd

df = pd.read_csv("mental_health_risk_dataset.csv")

# Проверим частоты категорий, чтобы увидеть, есть ли редкие
for col in ['gender', 'marital_status', 'education_level', 'employment_status']:
    print(f"\nЧастоты для {col}:")
    print(df[col].value_counts())

# Средние психологические показатели по статусу занятости
agg_employment = df.groupby('employment_status').agg({
    'anxiety_score': ['mean', 'min', 'max'],
    'depression_score': 'mean',
    'stress_level': 'mean'
}).round(2)

print("\nАгрегированные показатели по статусу занятости:")
print(agg_employment)

# Количество записей в каждой группе
print("\nКоличество записей по семейному положению и образованию:")
print(df.groupby(['marital_status', 'education_level']).size())
