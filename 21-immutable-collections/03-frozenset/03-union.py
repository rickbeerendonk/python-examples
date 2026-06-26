# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

fst1 = frozenset({"A", "B"})
fst2 = frozenset({"B", "C"})

result = fst1.union(fst2)

for item in sorted(result):
    print(item)

# A
# B
# C