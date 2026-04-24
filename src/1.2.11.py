#!/usr/bin/env python
import pandas as pd

df = pd.read_csv("mental_health_risk_dataset.csv")

print("Уникальные значения в поле gender:")
print(df['gender'].unique())
print("\nУникальные значения в поле marital_status:")
print(df['marital_status'].unique())

categorical_cols = ['gender', 'marital_status', 'education_level', 'employment_status']
for col in categorical_cols:
    df[col] = df[col].str.strip().str.lower()

# Возрастные группы
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

# Категории тревожности
def anxiety_cat(val):
    if val <= 3:
        return 'Низкий'
    elif val <= 6:
        return 'Средний'
    else:
        return 'Высокий'

df['anxiety_category'] = df['anxiety_score'].apply(anxiety_cat)

df_dummies = pd.get_dummies(df,
                            columns=['gender', 'marital_status', 'age_group', 'anxiety_category'],
                            drop_first=True)

print("\nКоличество признаков после one-hot кодирования:", df_dummies.shape[1])
