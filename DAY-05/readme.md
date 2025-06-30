# 🌲 Day 05: Decision Trees & Random Forests – Lung Capacity Classification

## 📌 Task Objective
To understand and implement **tree-based models** for **binary classification** using `Smoke` (Yes/No) as the target.

We trained and compared a **Decision Tree** and a **Random Forest** to classify whether a person is a smoker based on lung capacity data.

---

## 🗂️ Dataset Overview

- **Dataset:** LungCapData.csv
- **Rows:** 725
- **Target Column:** `Smoke` (Yes/No → 1/0)
- **Type:** Binary Classification

| Feature       | Description                          |
|---------------|--------------------------------------|
| `LungCap`     | Lung capacity (numeric)              |
| `Age`         | Age of subject                       |
| `Height`      | Height of subject                    |
| `Gender`      | Encoded (0/1)                        |
| `Caesarean`   | Born via C-section (encoded)         |

---

## 🛠️ Tools Used

- `pandas`, `numpy` – Data processing  
- `scikit-learn` – Modeling and evaluation  
- `seaborn`, `matplotlib` – Visualization

---

## 🔁 Workflow Summary

### 1. Preprocessing
- Dropped `Unnamed: 0` (index column)
- Encoded:
  - `Smoke`, `Gender`, `Caesarean` as binary (0/1)

### 2. Model 1: Decision Tree
- Trained basic `DecisionTreeClassifier`
- Visualized using `plot_tree`
- Evaluated with accuracy & classification report
- Re-trained with `max_depth=3` to control overfitting

### 3. Model 2: Random Forest
- Trained `RandomForestClassifier` with 100 trees
- Compared performance with Decision Tree
- Analyzed **feature importances**

### 4. Cross-Validation
- Performed 5-fold cross-validation on Random Forest
- Calculated average accuracy

---

## ✅ Results

| Model              | Accuracy | Notes                          |
|-------------------|----------|--------------------------------|
| Decision Tree      | ~88%     | Simple model                   |
| Decision Tree (Depth 3) | ~85% | Less overfitting               |
| Random Forest      | ~91%     | Best performance               |
| Random Forest (CV) | ~90%     | Stable across folds            |

---

## 📊 Key Visuals

- 📌 **Decision Tree Plot**  
- 📌 **Random Forest Feature Importances**  
- 📌 **Confusion Matrices**  
- 📌 **Cross-Validation Scores**

---

## 🧠 Learnings

- Tree models are easy to interpret and visualize
- Decision Trees can **overfit** without depth control
- Random Forests are **more accurate and robust**
- Feature importances help understand what drives predictions

---

