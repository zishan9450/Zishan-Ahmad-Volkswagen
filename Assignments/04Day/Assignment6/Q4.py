# 4. Translate to rövarspråket
def translate(text):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in text:
        if char.isalpha() and char not in vowels:
            result += char + "o" + char.lower()
        else:
            result += char
    
    return result

text = input("Enter text: ")
translated = translate(text)
print(f"Translated: {translated}")
