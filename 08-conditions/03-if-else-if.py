# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

from datetime import datetime

moment = datetime.now()
hour = moment.hour

if hour < 6:
    print("Good night")
elif hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
else:
    print("Good evening")