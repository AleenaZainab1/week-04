import pandas as pd
import matplotlib.pyplot as plt

# ------------ Task 1: Bar chart of marks per student ------------
df = pd.read_csv("student.csv")

# Missing values ko 0 se replace kar do
df = df.fillna(0)

# Har student ke total marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# Bar chart
plt.bar(df["Name"], df["Total"])
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Marks per Student")
plt.show()


# ------------ Task 2: Line chart of monthly sales ------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [10000, 12000, 9000, 15000, 18000, 16000]

plt.plot(months, sales, marker="o")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales of Company")
plt.show()
