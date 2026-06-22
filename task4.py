import pandas as pd
import matplotlib.pyplot as plt

cols = [
    "Severity",
    "Start_Time",
    "Start_Lat",
    "Start_Lng",
    "Temperature(F)",
    "Visibility(mi)",
    "Wind_Speed(mph)",
    "Weather_Condition",
    "State",
    "Sunrise_Sunset"
]

df = pd.read_csv("US_Accidents_March23.csv", usecols=cols)

print(df.head())
print(df.info())
print(df.isnull().sum())

df["Start_Time"] = pd.to_datetime(
    df["Start_Time"],
    format="mixed",
    errors="coerce"
)

df["Hour"] = df["Start_Time"].dt.hour

plt.figure(figsize=(7, 5))
df["Severity"].value_counts().sort_index().plot(kind="bar")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.title("Severity Distribution")
plt.savefig("severity_distribution.png")
plt.close()

plt.figure(figsize=(10, 5))
df["Weather_Condition"].value_counts().head(10).plot(kind="bar")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.title("Top 10 Weather Conditions")
plt.tight_layout()
plt.savefig("weather_conditions.png")
plt.close()

hourly_accidents = df["Hour"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
hourly_accidents.plot()
plt.xlabel("Hour of Day")
plt.ylabel("Number of Accidents")
plt.title("Accidents by Time of Day")
plt.savefig("hourly_accidents.png")
plt.close()

plt.figure(figsize=(10, 5))
df["State"].value_counts().head(10).plot(kind="bar")
plt.xlabel("State")
plt.ylabel("Count")
plt.title("Top 10 States by Accidents")
plt.tight_layout()
plt.savefig("state_accidents.png")
plt.close()

sample = df.sample(100000, random_state=42)

plt.figure(figsize=(8, 6))
plt.scatter(
    sample["Start_Lng"],
    sample["Start_Lat"],
    s=1,
    alpha=0.2
)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Accident Hotspots")
plt.savefig("accident_hotspots.png")
plt.close()

print("Task 4 completed successfully")