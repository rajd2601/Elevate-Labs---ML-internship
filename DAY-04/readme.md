# 🧠 Day 04: Logistic Regression – Raisin Type Classification

## 📌 Task Objective
Build a **binary classification model** using **Logistic Regression** to predict the type of raisin — either `Kecimen` or `Besni` — based on shape and size features.

---

## 🗂️ Dataset Overview

- **Dataset:** Raisin_Dataset.csv
- **Total Rows:** 900
- **Target Column:** `Class` (Categorical: `Kecimen` or `Besni`)
- **Type:** Binary Classification

### 🔢 Features Used
| Feature            | Description                                  |
|--------------------|----------------------------------------------|
| Area               | Surface area of the raisin                   |
| MajorAxisLength    | Major axis of ellipse fitted to raisin       |
| MinorAxisLength    | Minor axis of ellipse                        |
| Eccentricity       | Roundness of the raisin                      |
| ConvexArea         | Area of the convex hull                      |
| Extent             | Area / bounding box area                     |
| Perimeter          | Length of the outer edge of the raisin       |

---

## 🛠️ Tools & Libraries
- `pandas`, `numpy` – Data handling  
- `matplotlib`, `seaborn` – Visualizations  
- `scikit-learn` – Model building, scaling, and evaluation

---

## 🔁 Workflow Summary

### ✅ Step 1: Load & Explore Data
- Loaded data from CSV
- Explored class distribution

### ✅ Step 2: Preprocessing
- Encoded target column using `LabelEncoder`
- Standardized features with `StandardScaler`

### ✅ Step 3: Train-Test Split
- 80% training, 20% testing

### ✅ Step 4: Model Training
- Fitted `LogisticRegression()` model from `scikit-learn`

### ✅ Step 5: Model Evaluation
- Calculated:
  - **Accuracy**
  - **Precision**
  - **Recall**
  - **ROC-AUC Score**
- Generated:
  - **Confusion Matrix**
  - **Classification Report**
  - **ROC Curve**

### ✅ Step 6: Threshold & Sigmoid Function
- Explained sigmoid:  
  `sigmoid(z) = 1 / (1 + e^(-z))`
- Tuned threshold using ROC curve for better control over precision/recall

---

## ✅ Results

| Metric       | Score (approx) |
|--------------|----------------|
| Accuracy     | 95%            |
| Precision    | 96%            |
| Recall       | 95%            |
| ROC-AUC      | 99%            |

---

## 📊 Visuals

- ✅ **Confusion Matrix** – Shows true vs. predicted classes  
- ✅ **ROC Curve** – Helps visualize trade-off between sensitivity and specificity  
- ✅ **Classification Report** – Includes F1-Score

---

## 📬 Conclusion

The logistic regression model performs **extremely well** in classifying raisin types with minimal preprocessing. This task helped strengthen understanding of:
- How logistic regression works
- How to evaluate classification models
- The role of the sigmoid function and decision thresholds

