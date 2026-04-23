#!/usr/bin/env python
import pandas as pd

df = pd.read_csv("mental_health_risk_dataset.csv")

print("Размер данных до удаления дубликатов:", df.shape)

duplicates = df.duplicated()
print("Количество дубликатов:", duplicates.sum())

if duplicates.sum() > 0:
    df = df.drop_duplicates()
    print("Дубликаты удалены. Новый размер:", df.shape)
else:
    print("Дубликаты не найдены.")

# df.to_csv("mental_health_risk_clean.csv", index=False)
