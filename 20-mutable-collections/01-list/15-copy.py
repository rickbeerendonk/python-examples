# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

lst = ["A", "B", "C"]

new_lst = lst.copy()  # Creates a shallow copy
new_lst.append("D")

for item in lst:
    print(item)

# A
# B
# C

for item in new_lst:
    print(item)

# A
# B
# C
# D