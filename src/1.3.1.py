#!/usr/bin/env python
import pandas as pd

df = pd.read_csv("mental_health_risk_dataset.csv")

gender_map = {'Male': 'Мужчина', 'Female': 'Женщина', 'Other': 'Другой'}
marital_map = {'Single': 'Холост / не замужем', 'Married': 'В браке', 'Divorced': 'Разведён(а)'}
education_map = {'High School': 'Среднее', 'Bachelor': 'Бакалавр', 'Master': 'Магистр', 'PhD': 'Доктор'}
employment_map = {'Employed': 'Работает', 'Unemployed': 'Безработный', 'Self-Employed': 'Самозанятый', 'Student': 'Студент'}

mapping = {
    'gender': gender_map,
    'marital_status': marital_map,
    'education_level': education_map,
    'employment_status': employment_map
}

print("Категории признаков:")
for col in ['gender', 'marital_status', 'education_level', 'employment_status']:
    unique_vals = df[col].unique()
    translated = [mapping[col].get(val, val) for val in unique_vals]
    print(f"\n{col}: {translated}")

binary_cols = ['panic_attack_history', 'family_history_mental_illness',
               'previous_mental_health_diagnosis', 'therapy_history', 'substance_use']
binary_translation = {0: 'Нет', 1: 'Да'}
print("\nБинарные признаки:")
for col in binary_cols:
    unique_vals = df[col].unique()
    translated = [binary_translation.get(val, val) for val in unique_vals]
    print(f"{col}: {translated}")
