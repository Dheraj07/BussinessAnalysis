from src.preprocessing import load_and_preprocess_data
from src.clustering import perform_clustering
from src.visualize import plot_clusters

# Load and preprocess data
file_path = "data/bank_transactions.csv"
customer_spending = load_and_preprocess_data(file_path)

# Perform clustering
customer_spending, model = perform_clustering(customer_spending)

# Visualize clusters
plot_clusters(customer_spending)

# Display cluster stats
print(customer_spending.groupby("Cluster").mean())
