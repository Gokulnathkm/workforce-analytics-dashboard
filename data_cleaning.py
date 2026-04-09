import pandas as pd

# Load dataset
df = pd.read_csv("Extended_Employee_Performance_and_Productivity_Data.csv")

# Basic cleaning
df.drop_duplicates(inplace=True)
df.ffill(inplace=True)

# Convert data types (example)
df['Age'] = df['Age'].astype(int)

# Save cleaned dataset
df.to_csv("cleaned_employee_data.csv", index=False)

print("Data cleaned and saved successfully!")
