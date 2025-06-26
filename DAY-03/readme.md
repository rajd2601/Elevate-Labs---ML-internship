# 🌡️ Day 03: Linear Regression – Seattle Weather Dataset

## 📌 Task Objective
To implement and understand **simple and multiple linear regression** using the Seattle Weather dataset. The goal is to predict the **maximum temperature (`temp_max`)** based on features like **minimum temperature, wind speed, and precipitation**.

---

## 🗂️ Dataset Overview

- **Rows:** 1461
- **Columns:** 6  
- **Target Variable:** `temp_max`  
- **Independent Variables:** `temp_min`, `precipitation`, `wind`

| Column         | Description                    |
|----------------|--------------------------------|
| `temp_max`     | Daily max temperature (°C)     |
| `temp_min`     | Daily min temperature (°C)     |
| `precipitation`| Rainfall in mm                 |
| `wind`         | Wind speed in m/s              |
| `weather`      | Weather description (dropped)  |
| `date`         | Date of record (dropped)       |

---

## 🛠️ Tools Used

- `pandas`, `numpy` – Data handling
- `scikit-learn` – Model building & evaluation
- `matplotlib`, `seaborn` – Data visualization

---

## 🔁 Task Workflow

### 1. Data Preprocessing
- Dropped non-numeric columns (`weather`, `date`)
- Checked for missing values – none found

### 2. Feature & Target Selection
- Features: `temp_min`, `precipitation`, `wind`
- Target: `temp_max`

### 3. Train-Test Split
- Used 80% data for training, 20% for testing
- `train_test_split` from `sklearn`

### 4. Model Training
- Used `LinearRegression()` from `sklearn.linear_model`
- Trained the model on training data

### 5. Evaluation Metrics
- **MAE** (Mean Absolute Error)
- **MSE** (Mean Squared Error)
- **R² Score**

### 6. Visualization
- Plotted **actual vs predicted** `temp_max` values
- Plotted **regression line**
- Displayed model coefficients and intercept

---

## ✅ Sample Results

| Metric       | Value      |
|--------------|------------|
| MAE          | ~1.53      |
| MSE          | ~4.12      |
| R² Score     | ~0.91      |

> 🔍 The model shows a strong fit, with R² close to 1. The temperature is most influenced by `temp_min`.

---

## 📊 Coefficient Interpretation

| Feature        | Coefficient |
|----------------|-------------|
| `temp_min`     | +0.84       |
| `precipitation`| -0.23       |
| `wind`         | -0.15       |

- A higher `temp_min` typically leads to a higher `temp_max`.
- Rain and wind have mild negative impact on the daily high temperature.

---

## 📬 Notes

- This regression model provides a strong baseline.
- Further improvement may come from feature engineering (e.g., seasonal variables).
