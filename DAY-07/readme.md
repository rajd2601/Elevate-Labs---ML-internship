# 🧬 Day 07: Support Vector Machines (SVM) – Breast Cancer Classification

## 📌 Task Objective
To implement and evaluate **Support Vector Machine (SVM)** classifiers for identifying whether a tumor is **malignant** or **benign** using the **Breast Cancer dataset**.

---

## 🗂️ Dataset Overview

- **Dataset:** breast-cancer.csv
- **Rows:** 569
- **Target Column:** `diagnosis`  
  - `M` = Malignant (1)  
  - `B` = Benign (0)
- **Features:** 30 numerical attributes
- **Dropped Column:** `id` (non-informative)

---

## 🛠️ Tools & Libraries

- `pandas`, `numpy` – Data handling  
- `matplotlib`, `seaborn` – Visualization  
- `scikit-learn` – SVM modeling, preprocessing, tuning, evaluation  
- `Google Colab` – Development platform

---

## 🔁 Workflow Summary

### ✅ Step 1: Preprocessing
- Dropped `id` column
- Encoded `diagnosis` as binary (M = 1, B = 0)
- Normalized features using `StandardScaler`

### ✅ Step 2: Model Training
- Split data (80% train / 20% test)
- Trained two models:
  - `SVC(kernel="linear")`
  - `SVC(kernel="rbf")`

### ✅ Step 3: Hyperparameter Tuning
- Tuned `C` and `gamma` using `GridSearchCV` with 5-fold cross-validation
- Selected best parameters for `RBF` kernel

### ✅ Step 4: Model Evaluation
- Calculated:
  - Accuracy
  - Confusion Matrix
  - Classification Report
- Used `ConfusionMatrixDisplay` to visualize predictions
- Evaluated final model with **cross-validation**

---

## ✅ Results

| Model              | Accuracy |
|-------------------|----------|
| Linear SVM         | ~97%     |
| RBF SVM (default)  | ~98%     |
| RBF SVM (tuned)    | ~99%     |
| Cross-Validation   | ~98–99%  |

> The **tuned SVM with RBF kernel** outperformed the linear model with the best generalization performance.

---

## 📊 Visuals Included

- ✅ Confusion Matrix (Seaborn & sklearn display)  
- ✅ Classification Report for both kernels  
- ✅ GridSearchCV tuning report  

---

## 🧠 Learnings

- **SVMs** are highly effective for binary classification
- **RBF kernels** capture non-linear patterns better than linear kernels
- **Feature scaling** is essential for SVM performance
- **Hyperparameter tuning** significantly boosts accuracy
- **Cross-validation** ensures model stability

---

## 🚀 Next Step
Apply SVMs to multi-class datasets or experiment with kernels like `poly` or `sigmoid` to explore advanced capabilities.

