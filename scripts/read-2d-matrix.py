# Read integer 2d matrix from file
# and returns numpy array.
# Input file example:
# 123 32 ... 54
# ...
# 342 234 ... 23

import numpy as np

# Чтение файла и преобразование в массив NumPy
with open('data.txt', 'r') as f:
    data = [list(map(int, line.split())) for line in f]

array = np.array(data)
print(array)
