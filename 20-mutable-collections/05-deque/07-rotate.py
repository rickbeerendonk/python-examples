# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

from collections import deque

dq = deque(["A", "B", "C", "D"])

# Rotate the deque by 1 position to the right
dq.rotate(1)

for item in dq:
    print(item)

# D
# A
# B
# C