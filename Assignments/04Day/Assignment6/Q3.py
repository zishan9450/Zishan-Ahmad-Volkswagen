# 3. Dictionary with EVEN and ODD keys
numbers = []
for i in range(6):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

result = {'EVEN': [], 'ODD': []}

for num in numbers:
    if num % 2 == 0:
        result['EVEN'].append(num)
    else:
        result['ODD'].append(num)

print(result)
