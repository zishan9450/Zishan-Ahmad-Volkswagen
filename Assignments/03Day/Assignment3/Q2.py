# 2. Find repeated items in tuple
my_tuple = (1, 2, 3, 4, 2, 5, 6, 2, 7, 8, 3)
value = int(input("Enter value to find: "))
count = my_tuple.count(value)
if count > 0:
    print(f"{value} appears {count} times in the tuple")
else:
    print(f"{value} not found in the tuple")
