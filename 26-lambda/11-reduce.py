# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, n: acc + n, numbers)

print(total)  # 15