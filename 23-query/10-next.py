# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

numbers = [1, 3, 5, 8, 10]

first_even_number = next((n for n in numbers if n % 2 == 0), None)

print(first_even_number)  # 8