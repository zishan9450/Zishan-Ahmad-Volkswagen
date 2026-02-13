# 6. Count occurrence of each letter
text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."""

text_lower = text.lower()
letter_count = {}

for char in text_lower:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

sorted_letters = sorted(letter_count.items())
for letter, count in sorted_letters:
    print(f"{letter}: {count}")
