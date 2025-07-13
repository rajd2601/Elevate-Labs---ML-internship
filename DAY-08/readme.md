# 🛍️ Day 08: K-Means Clustering – Mall Customers Segmentation

## 📌 Task Objective
To perform **unsupervised learning** using the **K-Means clustering algorithm** to group mall customers into segments based on their purchasing behavior.

---

## 🗂️ Dataset Overview

- **Dataset:** Mall_Customers.csv
- **Rows:** 200 customers
- **Features Used:**
  - `Age`
  - `Annual Income (k$)`
  - `Spending Score (1–100)`
- **Dropped Columns:** 
  - `CustomerID` (irrelevant)
  - `Gender` (excluded for simplicity)

---

## 🛠️ Tools & Libraries

- `pandas`, `numpy` – Data handling  
- `matplotlib`, `seaborn` – Visualizations  
- `scikit-learn` – K-Means clustering, PCA, evaluation  

---

## 🔁 Workflow Summary

### ✅ Step 1: Preprocessing
- Removed `CustomerID` and `Gender`
- Standardized all numerical features using `StandardScaler`

### ✅ Step 2: Optimal K using Elbow Method
- Tried K from 1 to 10
- Plotted Within-Cluster Sum of Squares (WCSS)
- Identified **K = 5** as optimal (elbow point)

### ✅ Step 3: K-Means Clustering
- Fitted `KMeans(n_clusters=5)`
- Assigned cluster labels to each customer
- Added a `Cluster` column to the DataFrame

### ✅ Step 4: Evaluation
- Used **Silhouette Score** to measure clustering quality  
- Score for K=5 was **high**, indicating good separation

### ✅ Step 5: Visualization
- Applied **PCA** to reduce dimensions to 2D
- Visualized clusters in 2D with color-coded scatter plot

---

## ✅ Results

| Metric             | Value   |
|--------------------|---------|
| Optimal K          | 5       |
| Silhouette Score   | ~0.55–0.60 (varies) |
| Visualization      | 2D PCA plot with color-coded clusters |

---

## 📊 Visuals Included

- ✅ Elbow Method Curve  
- ✅ PCA-based Cluster Plot  
- ✅ Cluster Assignments in Final DataFrame  

---

## 🧠 Learnings

- **K-Means** is powerful for customer segmentation  
- **Standardization** is essential before clustering  
- **Elbow Method** helps estimate ideal number of clusters  
- **PCA** aids in clear and intuitive visualization  
- **Silhouette Score** is useful for evaluating clustering quality

---

## 🚀 Bonus Ideas

- Add `Gender` with proper encoding and check cluster distribution  
- Try **Hierarchical Clustering** or **DBSCAN** for comparison  
- Use real business cases like targeted marketing campaigns

