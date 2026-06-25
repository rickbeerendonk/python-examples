# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

lst = ["A", "B"]

lst.extend(["C", "D"])  # Adds all items from iterable

for item in lst:
    print(item)

# A
# B
# C
# D