import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("d:\\employee_productivity.xlsx")
df = pd.DataFrame(data)
print(df.head(11))


print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated("Employee_ID").sum())
print(df["Department"].value_counts())
print(df["Department"].nunique())

# 4. Summary Analysis
# ================================
print("\n--- Unique Values per Column ---")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# Top 5 Employees by Productivity
if "Productivity" in df.columns:
    print("\n--- Top 5 Productive Employees ---")
    print(df.nlargest(5, "Productivity")[["Employee_ID", "Employee_Name", "Productivity"]])

# Department-wise average productivity
if "Department" in df.columns and "Productivity" in df.columns:
    dept_summary = df.groupby("Department")["Productivity"].mean().reset_index()
    print("\n--- Department-wise Average Productivity ---")
    print(dept_summary)


# Gender-wise Salary analysis
if "Gender" in df.columns and "Salary" in df.columns:
    print("\n--- Gender-wise Average Salary ---")
    print(df.groupby("Gender")["Salary"].mean())
























# Department-wise average productivity
dept_summary = df.groupby("Department")["Productivity_Score"].mean().reset_index()
print(dept_summary)
plt.figure(figsize=(10,6))
sns.barplot(x = "Department", y = "Productivity_Score", data = dept_summary, palette = "viridis")
plt.title("Average Productivity score by Department")
plt.xlabel("Department")
plt.ylabel("Average Productivity Score")
plt.xticks(rotation=90)
plt.show()




salary_summary = df.groupby("Department")["Salary"].mean().reset_index()
print(salary_summary)
plt.figure(figsize = (6,4))
sns.boxplot(x = "Department", y = "Salary", data = salary_summary, palette = "viridis")
plt.title("Salary Distribution")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()



# Correlation Heatmap
plt.figure(figsize=(10,8))
corr = df.corr()
sns.heatmap(corr, annot = True, cmap = "coolwarm")
plt.title("Correlation Heatmap")
plt.show()