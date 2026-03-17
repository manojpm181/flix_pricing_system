import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_score


def create_clusters(df):
    print("🔍 Creating clusters (optimized)...")

    features = ['price', 'load', 'rating', 'reviews', 'rank']
    X = df[features].fillna(0)

    # ✅ SAMPLE FOR CLUSTER SELECTION
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
            batch_size=10000,
            n_init=10   # ✅ FIX WARNING
        )

        labels = model.fit_predict(X_sample_scaled)

        # ✅ SAFE SMALL RANDOM SAMPLE (NO MEMORY CRASH)
        try:
            sil_sample_size = min(2000, len(X_sample_scaled))
            idx = pd.Series(range(len(X_sample_scaled))).sample(
                sil_sample_size, random_state=42
            )

            small_sample = X_sample_scaled[idx]
            small_labels = labels[idx]

            score = silhouette_score(small_sample, small_labels)

        except Exception:
            print(f"⚠️ Skipping silhouette for k={k}")
            continue

        if score > best_score:
            best_score = score
            best_k = k

    print(f"✅ Best clusters: {best_k}")

    # ✅ FINAL MODEL ON FULL DATA
    final_model = MiniBatchKMeans(
        n_clusters=best_k,
        random_state=42,
        batch_size=10000,
        n_init=10
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
