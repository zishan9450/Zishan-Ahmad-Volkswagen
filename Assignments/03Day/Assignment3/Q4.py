# 4. Display elements thrice if number, else with '#'
mylist = ['41', 'DROND', 'BVSs', '13', 'ZARA']
for element in mylist:
    if element.isdigit():
        print(element * 3)
    else:
        print(element + '#')
