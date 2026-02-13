# 7. Convert integers and tuple to strings using map
int_list = [1, 2, 3, 4, 5]
int_tuple = (10, 20, 30, 40)

str_list = list(map(str, int_list))
str_tuple = list(map(str, int_tuple))

print(f"List of strings: {str_list}")
print(f"Tuple as list of strings: {str_tuple}")
