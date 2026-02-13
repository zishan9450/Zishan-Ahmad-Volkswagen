# 2. FizzBuzz using WHILE loops
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

num = start
while num <= end:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz!")
    elif num % 3 == 0:
        print("Fizz!")
    elif num % 5 == 0:
        print("Buzz!")
    else:
        print(num)
    num += 1
