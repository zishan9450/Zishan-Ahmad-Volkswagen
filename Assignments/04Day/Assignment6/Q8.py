# 8. Menu-driven program for shapes
import math

def circle_area(radius):
    return math.pi * radius * radius

def circle_perimeter(radius):
    return 2 * math.pi * radius

def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

print("=== Shape Calculator ===")
print("1. Circle")
print("2. Square")
print("3. Rectangle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    radius = float(input("Enter radius: "))
    area = circle_area(radius)
    perimeter = circle_perimeter(radius)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
elif choice == 2:
    side = float(input("Enter side: "))
    area = square_area(side)
    perimeter = square_perimeter(side)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
elif choice == 3:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = rectangle_area(length, width)
    perimeter = rectangle_perimeter(length, width)
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
else:
    print("Invalid choice!")
