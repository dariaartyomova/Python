import numpy as np
from scipy import stats
import time
def log(X, m, C):
    D = m.shape[0]
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)

    constant_term = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)

    X_centered = X - m
    exponent_term = -0.5 * np.sum(np.dot(X_centered, inv_C) * X_centered, axis=1)

    return constant_term + exponent_term

N = 10000
D = 3

X = np.random.rand(N, D)
m = np.random.rand(D)
C = np.random.rand(D, D)
C = np.dot(C, C.T)  # Делаем матрицу ковариаций положительно определенной

start_time = time.time()
result_custom = log(X, m, C)
custom_time = time.time() - start_time

start_time = time.time()
result_scipy = stats.multivariate_normal(m, C).logpdf(X)
scipy_time = time.time() - start_time

print("Custom implementation time:", custom_time)
print("Scipy implementation time:", scipy_time)



