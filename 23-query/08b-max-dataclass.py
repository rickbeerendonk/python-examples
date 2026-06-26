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

oldest = max(people, key=lambda p: p.age)

print(f"Oldest: {oldest}")  # Person(name='Bob', age=40)

last_by_name = max(people, key=lambda p: p.name)

print(f"Last by name: {last_by_name}")  # Person(name='Charlie', age=30)
