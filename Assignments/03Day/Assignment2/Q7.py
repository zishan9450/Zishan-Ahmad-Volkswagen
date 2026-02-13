# 7. Filter long words
def filter_long_words(words, len):
    result = []
    for word in words:
        if len(word) > len:
            result.append(word)
    return result

words = ["hello", "world", "python", "programming", "code"]
length = 5
filtered = filter_long_words(words, length)
print(filtered)
