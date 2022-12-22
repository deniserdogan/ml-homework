import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs

from kmeans import KMeans

X, y = make_blobs(centers=7, n_samples=500, n_features=2,
                  shuffle=True, random_state=42)


k = KMeans(maxK=8, max_iters=150, plot_steps=False)
y_pred = k.predict(X)
y_optimum = k.optimum(X)
