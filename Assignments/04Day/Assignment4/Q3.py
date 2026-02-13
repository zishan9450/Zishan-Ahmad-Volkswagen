# 3. Subtract (difference) of two lists
def subtract(list1, list2):
    result = []
    for element in list1:
        if element not in list2:
            result.append(element)
    return result

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
result = subtract(list1, list2)
print(f"Difference: {result}")
