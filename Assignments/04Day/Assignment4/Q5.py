# 5. Display unique characters in string
text = input("Enter a string: ")
char_list = list(text)
unique_chars = []
for char in char_list:
    if char not in unique_chars:
        unique_chars.append(char)
print(f"Unique characters: {unique_chars}")
