# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


people = [
    Person("Charlie", 30),
    Person("Alice", 25),
    Person("Bob", 40),
]

sorted_by_name = sorted(people, key=lambda p: p.name)

print("Sorted by name:")
for person in sorted_by_name:
    print(person)

# Sorted by name:
# Person(name='Alice', age=25)
# Person(name='Bob', age=40)
# Person(name='Charlie', age=30)

sorted_by_age = sorted(people, key=lambda p: p.age)

print("Sorted by age:")
for person in sorted_by_age:
    print(person)

# Sorted by age:
# Person(name='Alice', age=25)
# Person(name='Charlie', age=30)
# Person(name='Bob', age=40)
