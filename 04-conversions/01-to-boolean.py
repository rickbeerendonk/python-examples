# European Union Public License version 1.2
# Copyright © 2022 Rick Beerendonk

# Strings

print(bool("false"))  # True
print(bool("true"))   # True

print(bool(""))       # False
print(bool("other"))  # True

# Int

print(bool(0))  # False
print(bool(1))  # True

# Float

print(bool(0.0))  # False
print(bool(1.0))  # True

# Imaginary

print(bool(0j))  # False
print(bool(1j))  # True

# Imaginary

print(bool(None))  # False

# Ellipsis

print(bool(...))       # True
print(bool(Ellipsis))  # True
