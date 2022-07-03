"""
CP1404 Practical
Count word occurrences in a string
"""

word_to_count = {}
text = input("Text: ")  # text = "this is sentence or collection of words to be analyzed."

words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
words = list(word_to_count.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
