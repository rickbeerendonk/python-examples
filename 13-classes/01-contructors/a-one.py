# European Union Public License version 1.2
# Copyright © 2025 Rick Beerendonk

class Demo:
    def __init__(self, name, age=None):
        if age is None:
            age = 50
            print("Constructor (name) done")
        else:
            print("Constructor (name, age) done")
        self.name = name
        self.age = age

demo1 = Demo("one")
print(demo1.name)
print(demo1.age)
# Constructor (name) done
# one
# 50

demo2 = Demo("two", 20)
print(demo2.name)
print(demo2.age)
# Constructor (name, age) done
# two
# 20