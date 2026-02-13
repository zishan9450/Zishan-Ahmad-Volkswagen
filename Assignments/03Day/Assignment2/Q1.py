# 1. Factorial from 0 to 10
for num in range(11):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
