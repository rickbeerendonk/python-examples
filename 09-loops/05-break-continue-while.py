# European Union Public License version 1.2
# Copyright © 2025 Rick Beerendonk

i = 0

while i < 20:
    i += 1
    if i % 3 == 0:
        continue
    if i % 10 == 0:
        break
    print(i)

# 1
# 2
# 4
# 5
# 7
# 8