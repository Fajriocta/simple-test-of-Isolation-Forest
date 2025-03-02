from sklearn.ensemble import IsolationForest
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# ref : https://edistywn.medium.com/catatan-belajar-anomaly-detection-menggunakan-algoritma-isolation-forest-4e4d13e61c3d

data = load_iris(as_frame=True)
X, y = data.data, data.target
df = data.frame


# build model

"""
n_estimators adalah parameter yang digunakan untuk menentukan jumlah trees yang digunakan untuk pembuatan model.
contamination adalah parameter yang digunakan untuk menentukan proporsi dari anomaly dari dataset. Dapat dipahami juga bahwa parameter ini merupakan ambang batas suatu data dapat dikatakan anomaly atau bukan.
max_feature adalah parameter yang digunakan untuk menentukan jumah feature yang akan digunakan.
max_samples adalah jumlah sampel maksimum yang digunakan pada setiap feature.
"""
iforest = IsolationForest(n_estimators=100,
                          max_samples='auto',
                          contamination=0.05,
                          max_features=4,
                          bootstrap=False,
                          n_jobs=-1,
                          random_state=1)

pred = iforest.fit_predict(X)
df["Scores"] = iforest.decision_function(X)
df["anomaly_label"] = pred

# make viz

############

plt.figure(figsize=(8, 5))  # Ukuran gambar
plt.hist(df["Scores"], bins=30, color="blue", edgecolor="black", alpha=0.7)

plt.xlabel("Anomaly Scores")
plt.ylabel("Frequency")
plt.title("Histogram of Anomaly Scores")
plt.grid(axis="y", linestyle="--", alpha=0.7)  # Grid agar lebih mudah dibaca
plt.show()
