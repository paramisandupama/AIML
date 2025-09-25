import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("heart_disease.csv")  

# Columns to visualize
cols = ['Age', 'Blood Pressure', 'Cholesterol Level', 'BMI', 'Triglyceride Level', 
        'CRP Level', 'Homocysteine Level']

# BEFORE outlier removal
for col in cols:
    plt.figure(figsize=(8, 5))
    sns.boxplot(df[col])
    plt.title(f'Boxplot before outlier removal - {col}')
    plt.savefig(f'before_outlier_{col}.png')  # save the figure
    plt.close()


# AFTER outlier removal
for col in cols:
    plt.figure(figsize=(8, 5))
    sns.boxplot(df[col])  
    plt.title(f'Boxplot after outlier removal - {col}')
    plt.savefig(f'after_outlier_{col}.png')  
    plt.close()

