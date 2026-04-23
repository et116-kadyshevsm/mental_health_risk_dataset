#!/usr/bin/env python
import pandas as pd

df = pd.read_csv("mental_health_risk_dataset.csv")

print("Количество пропусков в каждом столбце:")
print(df.isnull().sum())
