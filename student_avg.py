import pandas as pd

#  Load CSV fileimport pandas as pd  

# CSV file load karna hy
df = pd.read_csv(r"C:\Users\ABXX\Desktop\week4\student.csv")

# Missing values ko 0 se fill karna hy (agar kahin NaN ho)
df = df.fillna(0)

# Har subject ka average calculate karna hy
averages = df.mean(numeric_only=True)

# Print results
print("Average marks for each subject:")
print(averages)
