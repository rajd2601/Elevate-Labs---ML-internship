This is a readme file and it contains some details of today's task.
Task 01- Data cleaning & pre processing : our main objective was to clean a dataset and prepare raw data for machine learning.
I used the titanic dataset as mentioned in the pdf.
As i have some prior knowledge about libraries used in ML, it was easy to use pandas, numpy, seaborn and matplotlib. 

Workflow : 
# 🧼 Day 1: Data Cleaning & Preprocessing – Titanic Dataset

## 📌 Task Objective
The goal of this task was to clean and preprocess the Titanic dataset to make it suitable for machine learning model development.

---

## 🔁 Workflow Summary

### 1. Load the Dataset
- Loaded the Titanic dataset using **Pandas**.
- Explored the basic structure using `.info()`, `.head()`, and `.isnull().sum()`.

### 2. Handle Missing Values
- Filled missing values in the `Age` column using the **median**.
- Filled missing values in the `Embarked` column using the **mode**.
- Dropped the `Cabin` column due to a high percentage of missing data.

### 3. Encode Categorical Features
- Converted categorical columns into numeric using **Label Encoding**:
- `Sex` → 0 (female), 1 (male)
- `Embarked` → Encoded as 0, 1, 2
- Dropped irrelevant textual features (`Name`, `Ticket`) for simplicity.

### 4. Normalize Numerical Features
- Scaled numerical features (`Age`, `Fare`, `Pclass`, etc.) using **StandardScaler** to ensure consistent value ranges.

### 5. Outlier Detection & Removal
- Used **Seaborn boxplots** to visualize outliers.
- Removed outliers using the **IQR (Interquartile Range)** method.

### 6. Save Cleaned Dataset
- Exported the cleaned dataset as `cleaned_titanic_dataset.csv` for future model training.

---

## 🛠️ Tools & Libraries Used
- **Python** (Google Colab)
- **Pandas**, **NumPy** – for data handling
- **Matplotlib**, **Seaborn** – for visualization
- **Scikit-learn** – for scaling and preprocessing

---

## ✅ Outcome
A fully cleaned and preprocessed Titanic dataset ready for machine learning tasks such as classification and prediction.

I have personally used AI tools to assist my work, it helps me to get a better understanding of the whole scenario and solve my doubts. 
