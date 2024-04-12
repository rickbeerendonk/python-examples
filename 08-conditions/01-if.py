# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

from datetime import datetime

moment = datetime.now()
hour = moment.hour

# One line
if hour < 6 or hour >= 18:
    print("Good night")

# Block
if 6 <= hour < 18:
    print("Good day")