def base_function():
    start = int(input("Enter start value: "))
    end = int(input("Enter end value: "))

    print("\nChoose option:")
    print("1. Print Odd Numbers")
    print("2. Print Even Numbers")
    print("3. Print All Numbers")

    choice = int(input("Enter your choice (1/2/3): "))
    return start, end, choice


def print_odd(start, end):
    print("\nOdd Numbers:")
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


def print_even(start, end):
    print("\nEven Numbers:")
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


def print_all(start, end):
    print("\nAll Numbers:")
    for i in range(start, end + 1):
        print(i, end=" ")
    print()
