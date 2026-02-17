import pandas as pd

# Load validated raw data
df_raw = pd.read_csv("C:/Users/Shrishti/Downloads/PROJECTS/Dashboard/ecommerce_transactions_validated.csv")

df = df_raw.copy()

# Convert date
df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'], errors='coerce')

# Drop critical nulls
df = df.dropna(subset=['Transaction_Date', 'Purchase_Amount'])

# Fix age
df['Age'] = df['Age'].fillna(df['Age'].median())
df = df[df['Age'] > 0]

# Fix purchase amount
df = df[df['Purchase_Amount'] > 0]

# Payment method
df['Payment_Method'] = df['Payment_Method'].fillna('Unknown')

# Derived columns
df['Year'] = df['Transaction_Date'].dt.year
df['Month'] = df['Transaction_Date'].dt.month
df['Month_Name'] = df['Transaction_Date'].dt.month_name()

df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[0, 18, 25, 35, 45, 60, 100],
    labels=['<18', '18-25', '26-35', '36-45', '46-60', '60+']
)

# Export cleaned data
df.to_csv("C:/Users/Shrishti/Downloads/PROJECTS/Dashboard/ecommerce_transactions_cleaned.csv", index=False)

print("Data transformed and saved successfully ✅")
