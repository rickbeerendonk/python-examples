# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

data = bytearray(b"AB")

data.extend(b"CD")

print(data)  # bytearray(b'ABCD')