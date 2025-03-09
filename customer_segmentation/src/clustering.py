from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def perform_clustering(data, n_clusters=4):
    X = data[["TotalSpending", "CustAccountBalance"]]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    data["Cluster"] = kmeans.fit_predict(X_scaled)

    return data, kmeans
