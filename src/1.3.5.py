#!/usr/bin/env python
import pandas as pd

df = pd.read_csv("mental_health_risk_dataset.csv")

def lifestyle_risk(row):
    if (row['physical_activity_hours_per_week'] <= 2 and
        row['screen_time_hours_per_day'] >= 8 and
        row['substance_use'] == 1):
        return 'Высокий риск'
    elif (row['physical_activity_hours_per_week'] <= 2 or
          row['screen_time_hours_per_day'] >= 8 or
          row['substance_use'] == 1):
        return 'Средний риск'
    else:
        return 'Низкий риск'

df['lifestyle_risk'] = df.apply(lifestyle_risk, axis=1)

print("Распределение новой категории lifestyle_risk:")
print(df['lifestyle_risk'].value_counts())

print("\nСредняя тревожность по lifestyle_risk:")
print(df.groupby('lifestyle_risk')['anxiety_score'].mean())
