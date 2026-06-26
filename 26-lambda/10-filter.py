# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

numbers = [1, 2, 3, 4, 5]

even_numbers = filter(lambda n: n % 2 == 0, numbers)

for number in even_numbers:
    print(number)

# 2
# 4