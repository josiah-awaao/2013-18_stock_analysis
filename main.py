import os


# Run Part 1: Benchmark Storage
print("\nRunning Storage Benchmarking (Part 1)...\n")
os.system("jupyter nbconvert --to notebook --execute src/13-18_benchmark_storage.ipynb")

# Run Part 2: Train Models & Save Predictions
print("\nRunning Stock Price Prediction (Part 2)...\n")
os.system("jupyter nbconvert --to notebook --execute src/13-18_feature_engineering.ipynb")

# Run Part 3: Start Streamlit Dashboard
print("\nLaunching Streamlit Dashboard (Part 3)...\n")
os.system("streamlit run src/dashboard.py")
