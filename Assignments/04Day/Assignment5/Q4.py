# 4. Random Password Generator
import random
import string

print("=== Random Password Generator ===")
length = int(input("Enter password length (8-16 recommended): "))

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special_chars = "!@#$%^&*"

password = []
password.append(random.choice(uppercase))
password.append(random.choice(lowercase))
password.append(random.choice(digits))
password.append(random.choice(special_chars))

all_chars = uppercase + lowercase + digits + special_chars
for i in range(length - 4):
    password.append(random.choice(all_chars))

random.shuffle(password)
final_password = ''.join(password)

print(f"\nGenerated Password: {final_password}")



# // Alternative version with CAPTCHA verification
# import random
# import string

# def generate_password(length):
#     uppercase = string.ascii_uppercase
#     lowercase = string.ascii_lowercase
#     digits = string.digits
#     special_chars = "!@#$%^&*"
    
#     password = []
#     password.append(random.choice(uppercase))
#     password.append(random.choice(lowercase))
#     password.append(random.choice(digits))
#     password.append(random.choice(special_chars))
    
#     all_chars = uppercase + lowercase + digits + special_chars
#     for i in range(length - 4):
#         password.append(random.choice(all_chars))
    
#     random.shuffle(password)
#     return ''.join(password)

# def generate_captcha(length=6):
#     chars = string.ascii_letters + string.digits
#     return ''.join(random.choice(chars) for i in range(length))

# print("=== Password Generator with CAPTCHA ===\n")

# print("Step 1: Generate Password")
# length = int(input("Enter password length (8-16): "))
# password = generate_password(length)
# print(f"Generated Password: {password}\n")

# print("Step 2: CAPTCHA Verification")
# captcha = generate_captcha(6)
# print(f"CAPTCHA: {captcha}")
# user_input = input("Retype CAPTCHA to confirm: ")

# if user_input == captcha:
#     print("\nCAPTCHA verified! Your password is ready to use.")
#     print(f"Final Password: {password}")
# else:
#     print("\nCAPTCHA verification failed! Password not confirmed.")
