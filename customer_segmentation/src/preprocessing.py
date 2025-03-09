import pandas as pd

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df["CustAccountBalance"].fillna(df["CustAccountBalance"].median(), inplace=True)

    customer_spending = df.groupby("CustomerID").agg(
        {"TransactionAmount (INR)": "sum", "CustAccountBalance": "mean"}
    ).reset_index()

    customer_spending.rename(columns={"TransactionAmount (INR)": "TotalSpending"}, inplace=True)
    return customer_spending
