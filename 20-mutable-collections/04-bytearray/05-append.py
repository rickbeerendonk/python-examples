# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

data = bytearray(b"AB")

data.append(ord("C"))

print(data)  # bytearray(b'ABC')