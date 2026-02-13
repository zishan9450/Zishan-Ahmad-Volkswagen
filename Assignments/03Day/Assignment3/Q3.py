# 3. Count elements until tuple is found
list1 = [10, 20, 30, (40, 50), 60]
count = 0
for element in list1:
    if isinstance(element, tuple):
        break
    count += 1
print(count)
