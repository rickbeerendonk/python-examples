# Copyright © 2026 Rick Beerendonk

print(bool(None))              # False

print(bool(0))                 # False
print(bool(1))                 # True

print(bool(""))                # False
print(bool("text"))            # True

print(bool([]))                # False
print(bool([1]))               # True

print(bool({}))                # False
print(bool({"key": "value"}))  # True