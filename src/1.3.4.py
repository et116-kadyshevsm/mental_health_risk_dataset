#!/usr/bin/env python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Создание папки для сохранения графиков
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# Загрузка данных
df = pd.read_csv("mental_health_risk_dataset.csv")

# Установка стиля
sns.set_style("whitegrid")

# Перевод категорий на русский язык для наглядности
gender_map = {'Male': 'Мужчина', 'Female': 'Женщина', 'Other': 'Другой'}
employ_map = {'Employed': 'Работает', 'Unemployed': 'Безработный',
              'Self-Employed': 'Самозанятый', 'Student': 'Студент'}
edu_map = {'High School': 'Среднее', 'Bachelor': 'Бакалавр',
           'Master': 'Магистр', 'PhD': 'Доктор'}

df_ru = df.copy()
df_ru['gender'] = df_ru['gender'].map(gender_map)
df_ru['employment_status'] = df_ru['employment_status'].map(employ_map)
df_ru['education_level'] = df_ru['education_level'].map(edu_map)

# ============================================================
# График 1: Часы сна vs Уровень тревожности
# ============================================================
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_ru, x='sleep_hours', y='anxiety_score',
                hue='gender', palette='Set2', alpha=0.7)
plt.title('Зависимость тревожности от продолжительности сна', fontsize=14)
plt.xlabel('Часы сна', fontsize=12)
plt.ylabel('Уровень тревожности', fontsize=12)
plt.legend(title='Пол')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'seaborn_sleep_vs_anxiety.png'))
plt.close()

# ============================================================
# График 2: Рабочий стресс vs Уровень депрессии
# ============================================================
plt.figure(figsize=(9, 5))
sns.scatterplot(data=df_ru, x='work_stress_level', y='depression_score',
                hue='employment_status', palette='viridis', alpha=0.7)
plt.title('Рабочий стресс и уровень депрессии', fontsize=14)
plt.xlabel('Уровень рабочего стресса', fontsize=12)
plt.ylabel('Уровень депрессии', fontsize=12)
plt.legend(title='Статус занятости', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'seaborn_workstress_vs_depression.png'))
plt.close()

# ============================================================
# График 3: Экранное время vs Физическая активность
# ============================================================
plt.figure(figsize=(9, 5))
sns.scatterplot(data=df_ru, x='screen_time_hours_per_day', y='physical_activity_hours_per_week',
                hue='education_level', palette='coolwarm', alpha=0.7)
plt.title('Экранное время и физическая активность', fontsize=14)
plt.xlabel('Экранное время (часов/день)', fontsize=12)
plt.ylabel('Физическая активность (часов/неделя)', fontsize=12)
plt.legend(title='Образование', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'seaborn_screen_vs_activity.png'))
plt.close()

# ============================================================
# Дополнительно: Парный график психологических показателей
# ============================================================
psych_vars = ['anxiety_score', 'depression_score', 'stress_level', 'mood_swings_frequency']
psych_labels = ['Тревожность', 'Депрессия', 'Стресс', 'Перепады настроения']
df_psych = df[psych_vars].copy()
df_psych.columns = psych_labels

sns.pairplot(df_psych, diag_kind='kde', plot_kws={'alpha':0.5})
plt.suptitle('Парный график психологических показателей', y=1.02, fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'seaborn_pairplot_psych.png'))
plt.close()
