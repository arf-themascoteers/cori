import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.switch_backend("Agg")

df = sns.load_dataset("iris")

print(df.head())
print(df.describe())
print(df.isnull().sum())

plt.figure(figsize=(6, 4))
plt.scatter(df["petal_length"], df["petal_width"], c="blue", alpha=0.5)
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Petal Length vs Petal Width")
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(df["sepal_length"], bins=10, color="green", edgecolor="black")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Distribution of Sepal Length")
plt.show()

sns.pairplot(df, hue="species", diag_kind="kde")
plt.show()
