# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

st = {"A", "B"}

st.update(["B", "C", "D"])

for item in sorted(st):
    print(item)

# A
# B
# C
# D