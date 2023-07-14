print("Enter a sequence of numbers separated by a space:")
list_of_elements = list(map(float, input().split()))
print("Entered numbers:")
print(list_of_elements)
temp_list = list()
for i in range(len(list_of_elements)):
    temp_list.append(list_of_elements[i])
    count = temp_list.count(list_of_elements[i])
    if count == 1:
        print(f"{list_of_elements[i]}, - NO")
    else:
        print(f"{list_of_elements[i]}, - YES")
