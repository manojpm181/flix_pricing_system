import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score


def create_clusters(df):
    print("🔍 Creating clusters (optimized)...")

    features = ['price', 'load', 'rating', 'reviews', 'rank']
    X = df[features].fillna(0)


    sample_size = min(50000, len(df))  
    X_sample = X.sample(sample_size, random_state=42)


    scaler = StandardScaler()
    X_sample_scaled = scaler.fit_transform(X_sample)


    best_k = 2
    best_score = -1

    for k in range(2, 8):  
        model = MiniBatchKMeans(
            n_clusters=k,
            random_state=42,
            batch_size=10000
        )

        labels = model.fit_predict(X_sample_scaled)

        
        small_sample = X_sample_scaled[:10000]
        small_labels = labels[:10000]

        score = silhouette_score(small_sample, small_labels)

        if score > best_score:
            best_score = score
            best_k = k

    print(f"✅ Best clusters: {best_k}")


    final_model = MiniBatchKMeans(
        n_clusters=best_k,
        random_state=42,
        batch_size=10000
    )

    X_scaled_full = scaler.transform(X)
    df['cluster'] = final_model.fit_predict(X_scaled_full)

    print("✅ Clustering Done (FAST 🚀)")

    return df


# #More mathematically correct
# #Finds “best k” using full data
# #Good for small datasets

# Extremely slow on 862K rows#

# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
# from sklearn.metrics import silhouette_score
# import numpy as np

# def create_clusters(df):
#     print("🔍 Creating clusters...")

#     features = ['price', 'load', 'rating', 'reviews', 'rank']
#     X = df[features].fillna(0)

#     scaler = StandardScaler()
#     X_scaled = scaler.fit_transform(X)

#     # 🔥 Find best K automatically
#     best_k = 2
#     best_score = -1

#     for k in range(2, 10):
#         model = KMeans(n_clusters=k, random_state=42, n_init=10)
#         labels = model.fit_predict(X_scaled)

#         score = silhouette_score(X_scaled, labels)

#         if score > best_score:
#             best_score = score
#             best_k = k

#     print(f"✅ Best clusters: {best_k}")

#     final_model = KMeans(n_clusters=best_k, random_state=42, n_init=10)
#     df['cluster'] = final_model.fit_predict(X_scaled)

#     print("✅ Clustering Done")
#     return df