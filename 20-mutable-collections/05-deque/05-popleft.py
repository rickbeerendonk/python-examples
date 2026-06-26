# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

from collections import deque

dq = deque(["A", "B", "C"])

item = dq.popleft()
print(item)  # A

print(dq)  # deque(['B', 'C'])