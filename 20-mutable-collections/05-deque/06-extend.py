# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

from collections import deque

dq = deque(["A", "B"])

dq.extend(["C", "D"])

for item in dq:
    print(item)

# A
# B
# C
# D