# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

from collections import deque

dq = deque(["A", "B"])

dq.append("C")

for item in dq:
    print(item)

# A
# B
# C