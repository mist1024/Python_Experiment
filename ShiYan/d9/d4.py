import numpy as np

from scipy import linalg


arr = np.array([[1,2,3],[2,2,1],[3,4,3]])

print('Inv:',linalg.inv(arr))