# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

# Booleans

print(float(True))  # 1.0
print(float(False)) # 0.0

# Int
print(float(123))  # 123.0

# String

print(float("123.456"))  # 123.456
print(float("1e2"))      # 100.0

# Exception: ValueError
try:
    print(float("other"))
except ValueError as e:
    print(f"Exception: {e}")  # Exception: could not convert string to float: 'other'

# Other: Imaginary - None - Ellipsis

# print(float(1j))  # TypeError: float() argument must be a string or a real number, not 'complex'
# print(float(None))  # TypeError: float() argument must be a string or a real number, not 'NoneType'
# print(float(...))  # TypeError: float() argument must be a string or a real number, not 'ellipsis'