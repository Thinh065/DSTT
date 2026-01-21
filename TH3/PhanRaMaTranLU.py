import numpy as np
from scipy import linalg
M = np.array([ [0.8, 0.3], [0.2, 0.7]])
P, L, U = linalg.lu(M) # lệnh lina.lu sẽ tách ma trận M thành 3 ma trận P, L và U
print("Ma trận P:\n", P)
print("Ma trận L:\n", L)
print("Ma trận U:\n", U)