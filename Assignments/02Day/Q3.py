# 3] 4 Digit Number Analysis
number = int(input("Enter a 4 digit number: "))

digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

print(f"a. {digit1} {digit2} {digit3} {digit4}")
print(f"b. {number} = {digit1}000 + {digit2}00 + {digit3}0 + {digit4}")
reversed_number = digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1
print(f"c. {reversed_number}")
