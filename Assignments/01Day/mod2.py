from mod1 import print_odd, print_even, print_all

start = int(input("Enter start value: "))
end = int(input("Enter end value: "))

print("\nChoose option:")
print("1. Print Odd Numbers")
print("2. Print Even Numbers")
print("3. Print All Numbers")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    print_odd(start, end)
elif choice == 2:
    print_even(start, end)
elif choice == 3:
    print_all(start, end)
else:
    print("Invalid choice!")
