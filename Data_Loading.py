import pandas as pd

df_raw = pd.read_csv(
    r"C:\Users\Shrishti\Downloads\PROJECTS\Dashboard\ecommerce_transactions.csv"
)

print("Raw data loaded")
print(df_raw.shape)

df_raw.to_csv(
    r"C:\Users\Shrishti\Downloads\PROJECTS\Dashboard\ecommerce_transactions_validated.csv",
    index=False
)
