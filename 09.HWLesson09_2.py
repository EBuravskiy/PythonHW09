print("Enter the number of elements in the first list of numbers, the size of the list must not exceed 100000 elements.")
size_list1 = int(input())
print("Enter the elements of the first list")
list1 = list()
for i in range(size_list1):
    element = float(input())
    list1.append(element)
print("Entered elements of the first list")
print(list1)

print("Enter the number of elements in the second list of numbers, the size of the list must not exceed 100000 elements.")
size_list2 = int(input())
print("Enter the elements of the second list")
list2 = list()
for i in range(size_list2):
    element = float(input())
    list2.append(element)
print("Entered elements of the first list")
print(list2)
set1 = set(list1)
set2 = set(list2)
result = set1.union(set2)
print("The number of numbers contained simultaneously in two lists:", len(result))
print(result)