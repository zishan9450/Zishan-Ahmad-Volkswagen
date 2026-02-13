# 5. Find longest word length
def find_longest_word(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

words = ["hello", "world", "python", "programming"]
length = find_longest_word(words)
print(f"Length of longest word: {length}")
