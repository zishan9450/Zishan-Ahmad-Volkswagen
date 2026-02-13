# 2. Union of two lists
def union(list1, list2):
    result = list1.copy()
    for element in list2:
        if element not in result:
            result.append(element)
    return result

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
result = union(list1, list2)
print(f"Union: {result}")
