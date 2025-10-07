# 👨‍💻 Employee Productivity Analysis — Python (Pandas, NumPy, Matplotlib, Seaborn)

## 🎯 Objective
The goal of this project is to analyze employee productivity data using Python.  
The analysis identifies the key factors affecting productivity, such as working hours, tasks completed, department performance, and experience level.

---

## 📂 Dataset Overview
**File Name:** `employee_productivity.xlsx`

**Columns Include:**
- Employee ID  
- Department  
- Gender  
- Age  
- Working Hours  
- Tasks Completed  
- Experience Level  
- Productivity Score  

---

## 🧹 Data Preparation
The dataset was cleaned and processed using **pandas** and **numpy** before analysis.

**Steps Performed:**
- Removed duplicates and missing values  
- Converted data types (e.g., date/time formats)  
- Created new calculated columns such as:
  - **Efficiency (%)** = Tasks Completed / Working Hours  
  - **Experience Category** = Junior / Mid / Senior  
- Handled outliers using IQR method  

---

## 📊 Exploratory Data Analysis (EDA)
EDA was performed to find patterns and relationships in the dataset.

### 🔍 Key Analyses:
- Average productivity by department  
- Impact of working hours on productivity  
- Gender-based performance comparison  
- Correlation between experience and tasks completed  

---

## 📈 Visualizations
The data was visualized using **Matplotlib** and **Seaborn** for clear insights.

| Chart Type         | Description                                |
|--------------------|--------------------------------------------|
| 📊 **Bar Plot**   | Department-wise average productivity        |
| 📈 **Line Chart** | Productivity vs Working Hours trend         |
| 🍩 **Pie Chart**  | Gender distribution                         |
| 🎯 **Boxplot**    | Productivity comparison by experience level |

---

## 🎨 Visualization Style
- **Color Theme:** Blue + Orange palette  
- **Background:** Light gray for better chart contrast  
- **Style Used:** Seaborn’s `whitegrid`  
- **Font Family:** Sans-serif (Roboto / Arial)  

---

## 💡 Key Insights
- Employees with **6–8 working hours** showed the **highest productivity levels**  
- **Senior employees** completed 30% more tasks than junior staff  
- **Marketing** and **Tech** departments were top performers  
- Gender had **minimal impact** on productivity scores  

---

## 🧰 Tools & Libraries Used
- **Python 3.10+**  
- **Pandas** — data cleaning and manipulation  
- **NumPy** — numerical analysis and calculations  
- **Matplotlib** — data visualization  
- **Seaborn** — statistical plots and styling  

---


![image alt](https://github.com/Daniyal07420/Python_Employee-Productivity/blob/main/Employee%20productivity(python).png?raw=true)
