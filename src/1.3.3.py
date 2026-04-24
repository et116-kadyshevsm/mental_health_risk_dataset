#!/usr/bin/env python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("mental_health_risk_dataset.csv")

le_gender = LabelEncoder()
df['gender_encoded'] = le_gender.fit_transform(df['gender'])

df = pd.get_dummies(df, columns=['marital_status'], prefix='marital', drop_first=True)

freq_enc = df['education_level'].value_counts(normalize=True)
df['education_freq'] = df['education_level'].map(freq_enc)

df = pd.get_dummies(df, columns=['employment_status'], prefix='employ', drop_first=True)

print(df[['gender', 'gender_encoded', 'education_level', 'education_freq']].head(10))
print("\nНовые столбцы после кодирования:")
print([col for col in df.columns if col.startswith('marital_') or col.startswith('employ_')])
