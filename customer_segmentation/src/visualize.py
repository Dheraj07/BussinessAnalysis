import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x=data["CustAccountBalance"],
        y=data["TotalSpending"],
        hue=data["Cluster"],
        palette="Set1",
        alpha=0.7
    )
    plt.title("Customer Segments Based on Spending & Account Balance")
    plt.xlabel("Customer Account Balance (INR)")
    plt.ylabel("Total Spending (INR)")
    plt.show()
