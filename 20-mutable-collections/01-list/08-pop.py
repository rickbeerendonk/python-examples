# European Union Public License version 1.2
# Copyright © 2025 Rick Beerendonk

lst = ["A", "B", "C", "D"]

removed = lst.pop(1)  # Removes the second item

print(f"Removed: {removed}")  # B

for item in lst:
    print(item)

# A
# C
# D