import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("traffic_data.csv")

print("🔹 First 5 Rows:")
print(df.head())

# Basic metrics
print("\n🔹 Average Page Views:", df['Page_Views'].mean())
print("🔹 Average Session Duration:", df['Session_Duration'].mean())
print("🔹 Average Bounce Rate:", df['Bounce_Rate'].mean())

# Group by traffic source
print("\n🔹 Traffic Source Analysis:")
print(df.groupby('Traffic_Source')['Page_Views'].mean())

# Visualization
plt.figure()
df['Traffic_Source'].value_counts().plot(kind='bar')
plt.title("Traffic Source Distribution")
plt.xlabel("Source")
plt.ylabel("Count")
plt.show()