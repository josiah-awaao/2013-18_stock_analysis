# Stock Analysis, Prediction, and Benchmarking

## Overview
This project involves **benchmarking stock data storage**, **applying machine learning models** to predict stock prices, and **visualizing results using a dashboard**. The dataset contains historical stock prices of S&P 500 companies from 2013-2018.

---

## 📂 Project Structure
```
Stock-Analysis/
│── src/                            # Source Code
│   ├── 13-18_benchmark_storage.ipynb  # Part 1: CSV vs. Parquet Benchmarking
│   ├── 13-18_feature_engineering.ipynb # Part 2: Technical Indicators & ML
│   ├── dashboard.py                # Part 3: Streamlit Dashboard
│── requirements.txt                # Dependencies (pip freeze > requirements.txt)
│── README.md                       # This file
│── main.py (Optional)              # Runs all parts automatically
```

---

## Installation
### ** 1 Install Dependencies**
```sh
pip install pandas polars scikit-learn ta matplotlib seaborn pyarrow fastparquet xgboost streamlit plotly
```

### ** 2 Clone Repository & Navigate**


### ** 3 Run Each Part Manually (Recommended)**
Run each Jupyter Notebook **one by one** inside Jupyter Lab or Notebook:

#### **Run Part 1: Storage Benchmarking**
```sh
jupyter notebook src/13-18_benchmark_storage.ipynb
```

#### **Run Part 2: Train Models & Save Predictions**
```sh
jupyter notebook src/13-18_feature_engineering.ipynb
```

#### **Run Part 3: Start Streamlit Dashboard**
```sh
streamlit run src/dashboard.py
or
streamlit run dashboard.py

```

### **(Optional) Run Everything with `main.py`**
```sh
python main.py
```
**  Note:** Running via `main.py` may take longer since it executes all notebooks sequentially.

---

## Part 1: Data Storage Benchmarking
### **Goal:** Compare CSV vs. Parquet for stock data storage.

### **Libraries Used & Why?**
- `pandas` – Load & process CSV files
- `polars` – Faster dataframe alternative for large datasets
- `pyarrow` & `fastparquet` – Efficient Parquet handling

### **Results Summary:**
| Scale  | CSV Read Time (s) | Parquet Read Time (s) | CSV Size (MB) | Parquet Size (MB) |
|--------|------------------|----------------------|--------------|-----------------|
| 1x     | ~2 sec           | ~0.5 sec            | 29 MB        | 8 MB            |
| 10x    | ~10 sec          | ~1.5 sec            | 290 MB       | 80 MB           |
| 100x   | ~50 sec          | ~5 sec              | 2.9 GB       | 800 MB          |

** Conclusion:** Parquet is significantly **faster & smaller** than CSV at large scales.

---

## Part 2: Data Analysis & Machine Learning
### **Goal:** Predict stock prices using machine learning.

### **Technical Indicators Used**
- **SMA (Simple Moving Average)** – Tracks trends
- **EMA (Exponential Moving Average)** – Reacts faster to price changes
- **RSI (Relative Strength Index)** – Detects overbought/oversold conditions
- **MACD (Moving Average Convergence Divergence)** – Identifies trend strength

### **ML Models Used & Why?**
- **Linear Regression** – Baseline model, simple but limited.
- **Random Forest** – Strong but slow for large datasets.
- **XGBoost** – Fast & accurate, best choice for large-scale ML.

### **Results (Mean Absolute Error - MAE)**
| Model             | MAE  |
|------------------|------|
| Linear Regression | 0.3057 |
| Random Forest    | 0.2978 |
| XGBoost         | 0.2644 ✅ Best |

** Conclusion:** XGBoost performed best due to its ability to handle non-linearity.

---

## Part 3: Dashboard Visualization
### **Goal:** Create an interactive dashboard for:
1. **Benchmark results (CSV vs. Parquet)**
2. **Stock price predictions (by company)**

### **Library Chosen: Streamlit (Why?)**
**Easier to use** than Dash/Reflex
**Faster setup**, simple Python-based UI
**Supports interactive charts with Plotly**

### **Run the Dashboard:**
```sh
streamlit run src/dashboard.py
```

### **Features:**
-  **Shows benchmarking results** as interactive bar charts.
-  **Allows searching for company stock predictions**.
-  **Displays actual vs. predicted stock prices** in a table & graph.

---

##  Final Thoughts & Recommendations
- **Use Parquet** for scalable data storage.
- **XGBoost is the best model** for stock price prediction.
- **Streamlit makes dashboarding simple & effective.**

