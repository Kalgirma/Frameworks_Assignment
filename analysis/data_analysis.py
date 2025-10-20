import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

print(df.info())
print(df.isnull().sum())

year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.show()
