print("Enter a sequence of numbers separated by a space:")
list_of_elements = list(map(float, input().split()))
print("Entered numbers:")
print(list_of_elements)
unique_elements = set(list_of_elements)
print("Unique elements:")
print(unique_elements)
for i in unique_elements: 
    exist_count = list_of_elements.count(i)
    if exist_count > 1:
        print(i, "- YES! The number", i, "occurred", exist_count, "times in the entered sequence.")
    else:
        print(i, "- NO! The number", i, "did not occur in the entered sequence of numbers")
