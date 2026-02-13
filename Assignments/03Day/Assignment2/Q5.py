# 5. Function to check overlapping lists
def overlapping(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
list3 = [10, 11, 12]
print(overlapping(list1, list2))
print(overlapping(list1, list3))
