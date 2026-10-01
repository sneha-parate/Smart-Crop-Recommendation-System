import pandas as pd

# Reading the dataset
data = pd.read_csv("Crop_recommendation.csv")

# Taking input from user
N = float(input("Enter Nitrogen (mg/kg): "))
P = float(input("Enter Phosphorus (mg/kg): "))
K = float(input("Enter Potassium (mg/kg): "))
temperature = float(input("Enter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))
ph = float(input("Enter pH: "))
rainfall = float(input("Enter Rainfall (mm): "))

# Finding similar rows from the dataset
match = data[
    (data["N"] >= N - 10) &
    (data["N"] <= N + 10) &
    (data["P"] >= P - 10) &
    (data["P"] <= P + 10) &
    (data["K"] >= K - 10) &
    (data["K"] <= K + 10) &
    (data["temperature"] >= temperature - 5) &
    (data["temperature"] <= temperature + 5) &
    (data["humidity"] >= humidity - 10) &
    (data["humidity"] <= humidity + 10) &
    (data["ph"] >= ph - 1) &
    (data["ph"] <= ph + 1) &
    (data["rainfall"] >= rainfall - 50) &
    (data["rainfall"] <= rainfall + 50)
]

# Recommending the most common crop
if len(match) > 0:
    recommendation = match["label"].value_counts().idxmax()
    print("\nRecommended Crop:", recommendation)
else:
    print("\nNo suitable crop found.")