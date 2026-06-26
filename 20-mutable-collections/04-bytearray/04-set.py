# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

data = bytearray(b"ABC")

data[1] = ord("D")

print(data)  # bytearray(b'ADC')