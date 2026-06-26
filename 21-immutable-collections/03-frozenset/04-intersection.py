# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

fst1 = frozenset({"A", "B", "C", "D", "E"})
fst2 = frozenset({"B", "D", "F"})

result = fst1.intersection(fst2)

for item in sorted(result):
    print(item)

# B
# D