# 8] Telephone Bill Calculator
calls = int(input("Enter number of calls: "))

if calls <= 100:
    bill = 200
elif calls <= 150:
    bill = 200 + (calls - 100) * 0.60
elif calls <= 200:
    bill = 200 + 50 * 0.60 + (calls - 150) * 0.50
else:
    bill = 200 + 50 * 0.60 + 50 * 0.50 + (calls - 200) * 0.40

print(f"Monthly telephone bill: Rs. {bill}")
