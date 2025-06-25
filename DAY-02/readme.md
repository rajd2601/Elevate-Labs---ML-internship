# 📊 Day 02: Exploratory Data Analysis (EDA) – Food Expiry Tracker Dataset

## 📌 Task Objective
The goal of this task was to explore the `food_expiry_tracker.csv` dataset using statistical analysis and visualizations. The focus was on identifying trends, relationships, and anomalies that impact whether a food item is used before its expiry date.

---

## 🗂️ Dataset Description
The dataset contains 500 rows and 15 columns representing food items, their storage methods, purchase patterns, and whether or not they were used before expiry.

| Column Group       | Description |
|--------------------|-------------|
| `purchase_month`, `purchase_day_of_week` | Time of purchase (normalized) |
| `days_until_expiry`, `quantity`          | Shelf life & amount |
| `used_before_expiry`                     | ✅ Target variable (1 = used before expiry, 0 = wasted) |
| `item_*`                                 | Food categories (e.g., dairy, beverage) |
| `storage_*`                              | Storage location (e.g., freezer, fridge, pantry) |

---

## 🔁 EDA Workflow Summary

### 1. Summary Statistics
- Used `.describe()` to understand mean, median, std dev, and distribution of all numeric fields.
- Verified there were **no missing values** in the dataset.

### 2. Univariate Analysis
- Plotted histograms for all numerical features.
- Used boxplots to detect outliers in `days_until_expiry` and `quantity`.

### 3. Correlation & Relationships
- Used a **correlation heatmap** to observe relationships between features.
- Created a **pairplot** to visualize feature clusters based on the target label.

### 4. Trends & Patterns
- Items with fewer `days_until_expiry` were less likely to be used before expiry.
- `storage_fridge` and `storage_freezer` showed better usage rates than `pantry`.
- Some food categories (e.g., `item_dairy`, `item_fruit`) had higher wastage rates than others.

### 5. Visualizations
- Used `matplotlib` and `seaborn` for static plots.
- Used `plotly` for interactive histograms to analyze usage behavior dynamically.

---

## 🛠️ Tools & Libraries Used
- `pandas`, `numpy` – for data handling
- `matplotlib`, `seaborn` – for statistical plots
- `plotly.express` – for interactive visualization

---

## ✅ Key Takeaways
- EDA revealed meaningful trends between shelf life, storage method, and food wastage.
- Categorical encodings and correlations will help in feature selection for future modeling.
- Dataset is now well-understood and ready for preprocessing or model training.

