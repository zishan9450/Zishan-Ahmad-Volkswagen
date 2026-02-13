# 6. Find largest number without max()
n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    lst.append(num)

largest = lst[0]
for num in lst:
    if num > largest:
        largest = num

print(f"Largest number: {largest}")
