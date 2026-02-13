# 1. Intersection of two lists
def intersection(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
result = intersection(list1, list2)
print(f"Intersection: {result}")
