# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

values = [1, 2, 3, 4, 5, 6, 7]

# Multiple values
print(values[:])       # [1, 2, 3, 4, 5, 6, 7]
print(values[2:])      # [3, 4, 5, 6, 7]
print(values[:2])      # [1, 2]
print(values[:-2])     # [1, 2, 3, 4, 5]
print(values[-2:])     # [6, 7]
print(values[2:-2])    # [3, 4, 5]
print(values[-5:5])    # [3, 4, 5]
