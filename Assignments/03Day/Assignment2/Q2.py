# 2. Print alternate elements of list
n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    lst.append(element)

print("Alternate elements:")
for i in range(0, len(lst), 2):
    print(lst[i], end=" ")
