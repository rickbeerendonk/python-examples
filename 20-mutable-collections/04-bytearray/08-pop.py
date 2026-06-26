# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

data = bytearray(b"ABCD")

value = data.pop(1)
print(value)  # 66
print(data)  # bytearray(b'ACD')