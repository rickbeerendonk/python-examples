# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

dct = {"A": 1, "B": 2, "C": 3}

# Pop removes the key from the dictionary and returns the value.
value = dct.pop("B")

print(value)  # 2

for key, item_value in dct.items():
    print(f"{key}={item_value}")

# A=1
# C=3