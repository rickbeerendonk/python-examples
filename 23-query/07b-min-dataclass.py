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

youngest = min(people, key=lambda p: p.age)

print(f"Youngest: {youngest}")  # Person(name='Alice', age=25)

first_by_name = min(people, key=lambda p: p.name)

print(f"First by name: {first_by_name}")  # Person(name='Alice', age=25)
