# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

dct = {"A": 1, "B": 2, "C": 3}

dct["B"] = 20  # Change existing key
dct["D"] = 4  # Add new key

for key, value in dct.items():
    print(f"{key}={value}")

# A=1
# B=20
# C=3
# D=4