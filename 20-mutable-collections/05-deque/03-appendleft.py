# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

from collections import deque

dq = deque(["B", "C"])

dq.appendleft("A")

for item in dq:
    print(item)

# A
# B
# C