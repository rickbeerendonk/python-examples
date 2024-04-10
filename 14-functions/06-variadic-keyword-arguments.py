# European Union Public License version 1.2
# Copyright © 2024 Rick Beerendonk

def test(**kwargs):
  for key, value in kwargs.items(): 
    print("%s = %s" % (key, value)) 

  print()


def test2(*numbers, **kwargs):
  print("Variadic arguments:")
  for num in numbers:
    print("  %s" % num)

  print()

  print("Variadic keyword arguments:")
  for key, value in kwargs.items(): 
    print ("  %s = %s" % (key, value)) 

test(one=True, two=2, three="Three")
test2(1, 2, 3, four=True, five=5, six="Six")

# one = True
# two = 2
# three = Three
# 
# Variadic arguments:
#   1
#   2
#   3
# 
# Variadic keyword arguments:
#   four = True
#   five = 5
#   six = Six