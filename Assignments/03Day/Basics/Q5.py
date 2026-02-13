# 5. Count occurrence of '$' in string
str = "Hi, $I am the $ Symbol $99.99"
count = str.count('$')
print(f"Occurrence of '$': {count}")

# Alternative method using a loop
# str = "Hi, $I am the $ Symbol $99.99"
# count = 0
# for char in str:
#     if char == '$':
#         count += 1
# print(f"Occurrence of '$': {count}")
