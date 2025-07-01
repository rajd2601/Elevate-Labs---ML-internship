# 🌸 Day 06: K-Nearest Neighbors (KNN) – Iris Flower Classification

## 📌 Task Objective
To implement and evaluate the **K-Nearest Neighbors (KNN)** algorithm for classifying iris flower species based on their physical characteristics.

---

## 🗂️ Dataset Overview

- **Dataset:** Iris.csv
- **Rows:** 150
- **Target Column:** `Species` (Multiclass: Setosa, Versicolor, Virginica)
- **Features:**
  - `SepalLengthCm`
  - `SepalWidthCm`
  - `PetalLengthCm`
  - `PetalWidthCm`

---

## 🛠️ Tools Used

- `pandas`, `numpy` – Data handling  
- `matplotlib`, `seaborn` – Visualization  
- `scikit-learn` – KNN model, preprocessing, evaluation  
- `Google Colab` – Development environment  

---

## 🔁 Workflow Summary

### ✅ Step 1: Data Preparation
- Dropped unnecessary `Id` column
- Encoded `Species` into numerical format
- Normalized features using `StandardScaler`

### ✅ Step 2: Train-Test Split
- 80% training data, 20% testing data

### ✅ Step 3: Model Training
- Trained multiple `KNeighborsClassifier` models for **K = 1 to 10**
- Selected best value based on accuracy

### ✅ Step 4: Evaluation
- Calculated **accuracy**, **confusion matrix**, and **classification report**
- Plotted **confusion matrix heatmap**

### ✅ Step 5: Decision Boundary Visualization (Bonus)
- Visualized KNN decision boundary using only 2 features:  
  `PetalLengthCm` and `PetalWidthCm`  
- Used `matplotlib` and `ListedColormap` to plot 2D class regions

---

## ✅ Results

| K | Accuracy |
|---|----------|
| 3 | ~97%     |
| 5 | ~97%     |
| 7 | ~97%     |

> The model achieved **excellent performance** across all K values, especially for **K = 3–7**.

---

## 📊 Visuals

- ✅ Confusion Matrix Heatmap  
- ✅ Decision Boundary (2D) using Petal Features  
- ✅ Accuracy comparisons for different K values  

---

## 🧠 Learnings

- KNN is a **simple yet powerful** classification algorithm  
- **Scaling features** is crucial for distance-based models  
- Visualization helps in understanding **decision boundaries**  
- Model performance is **sensitive to K value** and **data distribution**

