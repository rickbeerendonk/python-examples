# European Union Public License version 1.2
# Copyright © 2026 Rick Beerendonk

words = ["pear", "apple", "fig", "banana"]

sorted_words = sorted(words, key=lambda word: len(word))

for word in sorted_words:
    print(word)

# fig
# pear
# apple
# banana