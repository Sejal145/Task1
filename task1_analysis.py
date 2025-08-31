
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('student-mat.csv', sep=';')

print(df.head())
print(df.isnull().sum())
print(df.dtypes)
print(df.shape)

df = df.drop_duplicates()

print("Average final grade (G3):", df['G3'].mean())
print("Students scoring above 15:", df[df['G3'] > 15].shape[0])
print("Correlation studytime vs G3:", df['studytime'].corr(df['G3']))
print(df.groupby('sex')['G3'].mean())

df['G3'].hist(bins=10)
plt.title("Histogram of Final Grades (G3)")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.show()

plt.scatter(df['studytime'], df['G3'])
plt.title("Study Time vs Final Grade (G3)")
plt.xlabel("Study Time (hours/week category)")
plt.ylabel("Final Grade (G3)")
plt.show()

df.groupby('sex')['G3'].mean().plot(kind='bar', color=['skyblue', 'lightcoral'])
plt.title("Average Final Grade (G3) by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Final Grade (G3)")
plt.show()
