import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---------------------------------------------------------
# 1. DATA CREATION & LOADING (Simulated robust AQI dataset)
# ---------------------------------------------------------
np.random.seed(42)
dates = pd.date_range(start="2025-01-01", periods=365)
cities = ["Delhi", "Mumbai", "Kolkata", "Bengaluru", "Chennai"]

data = []
for date in dates:
  for city in cities:
    if city in ["Delhi", "Kolkata"]:
      aqi = np.random.randint(120, 450)
    else:
      aqi = np.random.randint(50, 220)

    pm2_5 = aqi * np.random.uniform(0.45, 0.65)
    pm10 = pm2_5 * np.random.uniform(1.3, 1.7)
    no2 = np.random.randint(15, 85)
    data.append([date, city, aqi, pm2_5, pm10, no2])

df = pd.DataFrame(
    data, columns=["date", "city", "aqi_value", "pm2_5", "pm10", "no2"]
)

# ---------------------------------------------------------
# 2. DATA CLEANING & PREPROCESSING
# ---------------------------------------------------------
df.loc[df.sample(frac=0.02).index, "aqi_value"] = np.nan
df["aqi_value"] = df["aqi_value"].fillna(df["aqi_value"].median())
df["date"] = pd.to_datetime(df["date"])

# ---------------------------------------------------------
# 3. UNIVARIATE ANALYSIS: Distribution of AQI
# ---------------------------------------------------------
plt.figure(figsize=(9, 5))
plt.hist(
    df["aqi_value"], bins=35, color="#2b5c8f", edgecolor="black", alpha=0.85
)
plt.title("Distribution of Air Quality Index (AQI Values)", fontsize=14, pad=12)
plt.xlabel("AQI Value", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# ---------------------------------------------------------
# 4. BIVARIATE ANALYSIS: City-wise Pollution Comparison
# ---------------------------------------------------------
top_cities = (
    df.groupby("city")["aqi_value"].mean().sort_values(ascending=False)
)
plt.figure(figsize=(10, 5))
top_cities.plot(kind="bar", color="#e74c3c", edgecolor="black")
plt.title("Average AQI Across Major Cities", fontsize=14, pad=12)
plt.xlabel("City", fontsize=12)
plt.ylabel("Average AQI Value", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
