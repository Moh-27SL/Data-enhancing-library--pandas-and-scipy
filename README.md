# 🩸 Pima Indians Diabetes Data — Preprocessing & Enhancement

This project explores and preprocesses the **Pima Indians Diabetes Dataset** using `pandas` and `SciPy`.  
It demonstrates cleaning, outlier handling, standardization, and data splitting while preserving class balance.

---

## 📊 Dataset Information

**Shape:** (768, 9)  
**Columns:**

| Column | Non-Null Count | Dtype |
|---------|----------------|-------|
| Pregnancies | 768 | int64 |
| Glucose | 768 | int64 |
| BloodPressure | 768 | int64 |
| SkinThickness | 768 | int64 |
| Insulin | 768 | int64 |
| BMI | 768 | float64 |
| DiabetesPedigreeFunction | 768 | float64 |
| Age | 768 | int64 |
| Outcome | 768 | int64 |

---

## 📈 Data Description (Before Preprocessing)

| Statistic | Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI | DiabetesPedigreeFunction | Age | Outcome |
|------------|-------------|----------|----------------|----------------|----------|------|----------------------------|------|----------|
| **count** | 768 | 768 | 768 | 768 | 768 | 768 | 768 | 768 | 768 |
| **mean** | 3.85 | 120.89 | 69.10 | 20.54 | 79.80 | 31.99 | 0.47 | 33.24 | 0.35 |
| **std** | 3.37 | 31.97 | 19.36 | 15.95 | 115.24 | 7.88 | 0.33 | 11.76 | 0.48 |
| **min** | 0 | 0 | 0 | 0 | 0 | 0 | 0.078 | 21 | 0 |
| **max** | 17 | 199 | 122 | 99 | 846 | 67.1 | 2.42 | 81 | 1 |

### First 5 Samples (Before Preprocessing)

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI | DiabetesPedigreeFunction | Age | Outcome |
|-------------|----------|----------------|----------------|----------|------|----------------------------|------|----------|
| 6 | 148 | 72 | 35 | 0 | 33.6 | 0.627 | 50 | 1 |
| 1 | 85 | 66 | 29 | 0 | 26.6 | 0.351 | 31 | 0 |
| 8 | 183 | 64 | 0 | 0 | 23.3 | 0.672 | 32 | 1 |
| 1 | 89 | 66 | 23 | 94 | 28.1 | 0.167 | 21 | 0 |
| 0 | 137 | 40 | 35 | 168 | 43.1 | 2.288 | 33 | 1 |

---

## 🧼 Processing Steps

- Removed **zero values** from columns where zeros are **not physically possible** (e.g., `SkinThickness = 0` 😅).  
- **Clipped extreme outliers** (values beyond whiskers) to the whisker limits.  
- **Standardized all features** to ensure equal influence, since raw feature scales varied widely  
  (e.g., some ranged from 0–1, others from 0–200).  
- Standardization helps because most features roughly follow a **Gaussian distribution**.

---

## 📊 Data Description (After Processing)

| Statistic | Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI | DiabetesPedigreeFunction | Age | Outcome |
|------------|-------------|----------|----------------|----------------|----------|------|----------------------------|------|----------|
| **mean** | ~0 | ~0 | ~0 | ~0 | ~0 | ~0 | ~0 | ~0 | 0.35 |
| **std** | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0.48 |

### First 5 Samples (After Processing)

| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin | BMI | DiabetesPedigreeFunction | Age | Outcome |
|-------------|----------|----------------|----------------|----------|------|----------------------------|------|----------|
| 0.65 | 0.87 | -0.03 | 0.82 | 0.29 | 0.18 | 0.59 | 1.45 | 1 |
| -0.85 | -1.21 | -0.55 | 0.01 | 0.29 | -0.87 | -0.38 | -0.19 | 0 |
| 1.25 | 2.02 | -0.72 | 0.03 | 0.29 | -1.37 | 0.75 | -0.10 | 1 |
| -0.85 | -1.07 | -0.55 | -0.79 | -1.27 | -0.64 | -1.02 | -1.05 | 0 |
| -1.15 | 0.50 | -2.77 | 0.82 | 0.61 | 1.61 | 2.60 | -0.02 | 1 |

---

## 🔗 Correlation Between Features

| Feature | Outcome Correlation |
|----------|--------------------|
| Pregnancies | 0.22 |
| Glucose | **0.49** |
| BloodPressure | 0.17 |
| SkinThickness | 0.22 |
| Insulin | 0.27 |
| BMI | 0.31 |
| DiabetesPedigreeFunction | 0.18 |
| Age | 0.24 |

➡️ **Observation:** Glucose, BMI, and Insulin show the strongest relationships with diabetes outcome.

---

## ✂️ Data Splitting

Data was split into **training (80%)** and **testing (20%)** sets using **stratified sampling**  
to preserve the same proportion of diabetes outcomes across both sets.

> The splitting function returns `pandas` DataFrames: `X_train`, `X_test`, `y_train`, `y_test`.

---

## 🖼️ Visualizations

### Before Processing:
![Data Distribution](data_before_prepro.PNG)

### After Processing:
![Correlation Heatmap](correlation.PNG)  
![Data Distribution After Processing](data_after_processing.PNG)

---

## 🧩 Summary

✅ Cleaned impossible and extreme values  
✅ Standardized all features  
✅ Preserved class balance with stratified split  
✅ Achieved a Gaussian-like distribution suitable for modeling  

---

> “Good preprocessing is half the work — models just finish the job.”

---

