# 8. Calculate price with discount
quantity = int(input("Enter quantity: "))
unit_price = 5
total_price = quantity * unit_price

if quantity > 50:
    discount = total_price * 0.15
    final_price = total_price - discount
    print(f"Total: Rs {total_price}")
    print(f"Discount (15%): Rs {discount}")
    print(f"Final Price: Rs {final_price}")
elif quantity > 30:
    discount = total_price * 0.10
    final_price = total_price - discount
    print(f"Total: Rs {total_price}")
    print(f"Discount (10%): Rs {discount}")
    print(f"Final Price: Rs {final_price}")
else:
    print(f"Total Price: Rs {total_price}")
