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

grouped_age = df.groupby('age_group').agg({
    'anxiety_score': 'mean',
    'depression_score': 'mean',
    'stress_level': 'mean',
    'mood_swings_frequency': 'mean'
}).round(2)

print("Средние показатели по возрастным группам:")
print(grouped_age)

grouped_mar_edu = df.groupby(['marital_status', 'education_level']).agg({
    'anxiety_score': 'mean',
    'mental_health_risk': 'mean'
}).round(3)

print("\nСредняя тревожность и риск по семейному положению и образованию:")
print(grouped_mar_edu)
