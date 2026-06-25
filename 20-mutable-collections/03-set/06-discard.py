# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

st = {"A", "B", "C"}

st.discard("B")
st.discard("Z")  # No error when item does not exist

for item in sorted(st):
    print(item)

# A
# C