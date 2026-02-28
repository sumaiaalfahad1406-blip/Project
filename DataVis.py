import pandas as pd
import matplotlib.pyplot as plt

file_path = "C:/Users/lenovo/Downloads/knowledge graph of chronic pain.xlsx"
df = pd.read_excel(file_path)


# Top 10 Relations (Bar)
plt.figure()
df["relation"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Relations")
plt.xlabel("Relation")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()


# Top 10 Subjects (Bar)
plt.figure()
df["subject"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Subjects")
plt.xlabel("Subject")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()


# Number of Unique Values (Bar)
unique_counts = [
    df["subject"].nunique(),
    df["relation"].nunique(),
    df["object"].nunique()
]

plt.figure()
plt.bar(["Subjects", "Relations", "Objects"], unique_counts)
plt.title("Number of Unique Values")
plt.ylabel("Count")
plt.show()


# Relation Distribution (Pie)
plt.figure()
df["relation"].value_counts().head(6).plot(kind="pie", autopct="%1.1f%%")
plt.title("Relation Distribution (Top 6)")
plt.ylabel("")
plt.show()


# Triples per Subject (Histogram)
subject_counts = df["subject"].value_counts()

plt.figure()
plt.hist(subject_counts, bins=20)
plt.title("Triples per Subject")
plt.xlabel("Number of Triples")
plt.ylabel("Number of Subjects")
plt.show()


# Missing Values (Bar)
plt.figure()
df.isnull().sum().plot(kind="bar")
plt.title("Missing Values Per Column")
plt.ylabel("Missing Count")
plt.show()

print("Total Observations:", df.shape[0])
print("Total Features:", df.shape[1])