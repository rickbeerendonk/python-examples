# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

from datetime import datetime

moment = datetime.now()
hour = moment.hour

# if as an expression
str_value = "Good day" if 6 <= hour < 18 else "Good night"
print(str_value)