# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

values = [1, 2, 3, 4, 5, 6, 7]

# 1 value
print(values[0])       # 1
print(values[1])       # 2
print(values[2])       # 3
# print(values[-0])    # IndexError: list index out of range (Python doesn't allow -0 as a valid index)
print(values[-1])      # 7
print(values[-2])      # 6

# Multiple values
print(values[:])       # [1, 2, 3, 4, 5, 6, 7]
print(values[2:])      # [3, 4, 5, 6, 7]
print(values[:2])      # [1, 2]
print(values[:-2])     # [1, 2, 3, 4, 5]
print(values[-2:])     # [6, 7]
print(values[2:-2])    # [3, 4, 5]
print(values[-5:5])    # [3, 4, 5]