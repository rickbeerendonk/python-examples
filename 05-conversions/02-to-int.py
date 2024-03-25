# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

# Booleans

print(int(True))  # 1
print(int(False)) # 0

# Strings

print(int("10"))  # 10
# print(int(""))  # ValueError: invalid literal for int() with base 10: ''
# print(int("false"))  # ValueError: invalid literal for int() with base 10: 'false'

# Float

print(int(10.5))  # 10
print(int(0.0))   # 0

# Other: Imaginary - None - Ellipsis

# print(int(1j))  # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# print(int(None))  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
# print(int(...))  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'ellipsis'