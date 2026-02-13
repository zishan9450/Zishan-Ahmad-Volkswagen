# 8. Dictionary operations
people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

print(f"A. Number of students: {len(people)}")

people['Lisa'] = 'Red'
print(f"B. After changing Lisa's colour: {people}")

del people['Jenny']
print(f"C. After removing Jenny: {people}")

sorted_people = dict(sorted(people.items()))
print("D. Sorted by name:")
for name, colour in sorted_people.items():
    print(f"{name}: {colour}")
