# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

# Booleans

print(complex(True))  # (1 + 0j)
print(complex(False)) # 0j

# Int
print(complex(123))   # (123+0j)

# Float

print(complex(10.5))  # (10.5+0j)
print(complex(0.0))   # 0j

# String

print(complex("123"))  # (123+0j)
print(complex("1e2"))  # (100+0j)
print(complex("0j"))   # 0j
print(complex("1j"))   # 1j
print(complex("1+1j")) # (1+1j)

# Exception: ValueError
try:
    print(complex("other"))
except ValueError as e:
    print(f"Exception: {e}")  # complex() arg is a malformed string

# Other: None - Ellipsis

# print(complex(None))  # TypeError: complex() first argument must be a string or a number, not 'NoneType'
# print(complex(...))  # TypeError: complex() first argument must be a string or a number, not 'ellipsis'