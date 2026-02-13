# 7. Remove repetitive items from list
num = [2, 3, 4, 5, 2, 6, 3, 2]
result = []
for item in num:
    if item not in result:
        result.append(item)
print(f"Result: {result}")

# Alternative method using dict.fromkeys()
# num = [2, 3, 4, 5, 2, 6, 3, 2]
# result = list(dict.fromkeys(num))
# print(f"Result: {result}")
