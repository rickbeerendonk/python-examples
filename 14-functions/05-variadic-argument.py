# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

def test(text, *numbers):
    print(text)
    for number in numbers:
        print(number)

test("Hello Python", 1, 2, 3, 4)

# Hello Python
# 1
# 2
# 3
# 4