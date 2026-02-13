# 9. String operations menu
def even_position_chars(text):
    result = ""
    for i in range(0, len(text), 2):
        result += text[i]
    return result

def odd_position_chars(text):
    result = ""
    for i in range(1, len(text), 2):
        result += text[i]
    return result

def string_length(text):
    return len(text)

def add_a_times(text):
    length = len(text)
    return text + ('a' * length)

text = input("Enter a string: ")

print("\n=== Menu ===")
print("A. Display characters from even position")
print("B. Display characters from odd position")
print("C. Display length of a string")
print("D. Add 'a' at the end of string length times")

choice = input("Enter your choice (A/B/C/D): ").upper()

if choice == 'A':
    print(f"Even position characters: {even_position_chars(text)}")
elif choice == 'B':
    print(f"Odd position characters: {odd_position_chars(text)}")
elif choice == 'C':
    print(f"String length: {string_length(text)}")
elif choice == 'D':
    print(f"Result: {add_a_times(text)}")
else:
    print("Invalid choice!")
