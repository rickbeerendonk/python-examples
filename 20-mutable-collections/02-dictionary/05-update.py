# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

dct = {"A": 1, "B": 2}

# Update is different from assignment,
# ...because it can update multiple keys at once.
dct.update({"B": 20, "C": 3})

for key, value in dct.items():
    print(f"{key}={value}")

# A=1
# B=20
# C=3