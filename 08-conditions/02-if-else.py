# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

from datetime import datetime

moment = datetime.now()
hour = moment.hour

if 6 <= hour < 18:
    print("Good day")
else:
    print("Good night")