# 2. Frequency of numbers in list
List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 6, 2, 4, 2, 5, 23, 6, 4]
frequency = {}

for num in List1:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(f"Output: {frequency}")
