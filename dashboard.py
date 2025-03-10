# pip install streamlit dash plotly
# streamlit run dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

#LOAD DATA

# Load Benchmark Results (Ensure this file exists)
benchmark_file = "benchmark_results.csv"
try:
    benchmark_results = pd.read_csv(benchmark_file)
    st.write(f"Successfully loaded `{benchmark_file}`")
except FileNotFoundError:
    st.error(f"Error: `{benchmark_file}` not found! Run Part 1 first.")
    st.stop()

# Load Stock Predictions (Ensure this file exists)
predictions_file = "stock_predictions.csv"
try:
    predictions = pd.read_csv(predictions_file)
    st.write(f"Successfully loaded `{predictions_file}`")
except FileNotFoundError:
    st.error(f"Error: `{predictions_file}` not found! Run Part 2 first.")
    st.stop()

# Validate the dataset structure
required_columns = {"name", "date", "actual_close", "predicted_close"}
if not required_columns.issubset(predictions.columns):
    st.error(f"Error: `{predictions_file}` is missing required columns! Expected: {required_columns}")
    st.stop()

#benchmarking results

st.title("Stock Data Benchmarking & Predictions")

st.subheader("⚡ Benchmarking Results (CSV vs. Parquet)")
st.dataframe(benchmark_results)

# Plot Read/Write Times
fig_time = px.bar(
    benchmark_results, 
    x="Scale", 
    y=["CSV Read Time (s)", "Parquet Read Time (s)"],
    barmode="group", 
    title="📊 Read Time Comparison"
)
st.plotly_chart(fig_time)

fig_size = px.bar(
    benchmark_results, 
    x="Scale", 
    y=["CSV Size (MB)", "Parquet Size (MB)"],
    barmode="group", 
    title="📂 File Size Comparison"
)
st.plotly_chart(fig_size)

#stock predictions

st.subheader("Stock Price Prediction")

# Select company
companies = predictions["name"].unique()
company = st.selectbox("Select a company:", companies)

# Filter Data for Selected Company
company_data = predictions[predictions["name"] == company]

# Plot Actual vs Predicted Prices
fig_pred = px.line(
    company_data, 
    x="date", 
    y=["actual_close", "predicted_close"],
    labels={"value": "Stock Price", "date": "Date"},
    title=f"📊 Predicted vs. Actual Prices for {company}"
)
st.plotly_chart(fig_pred)

st.write("select a different company to see predictions.")

st.success("dashboard Loaded Successfully!")


