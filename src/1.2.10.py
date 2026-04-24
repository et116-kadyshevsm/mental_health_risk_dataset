#!/usr/bin/env python
import pandas as pd

df = pd.read_csv("mental_health_risk_dataset.csv")

def age_group(age):
    if age < 30:
        return '18-29'
    elif age < 40:
        return '30-39'
    elif age < 50:
        return '40-49'
    else:
        return '50+'

df['age_group'] = df['age'].apply(age_group)

def anxiety_cat(val):
    if val <= 3:
        return 'Низкий'
    elif val <= 6:
        return 'Средний'
    else:
        return 'Высокий'

df['anxiety_category'] = df['anxiety_score'].apply(anxiety_cat)

print("Распределение по возрастным группам:")
print(df['age_group'].value_counts())

print("\nРаспределение по категориям тревожности:")
print(df['anxiety_category'].value_counts())
