print("Enter number of elements from 1 to 100 000:")
elements = int(input())
if elements < 1 or elements > 100000:
    print("The number of elements entered does not match the condition. Try again.")
else:
    print("Enter elements separated by spaces from -2*10e9 to 2*10e9")
    list_of_elements = list(map(float, input().split())) #использован список, а не сразу множество, поскольку есть условие о количестве элементов
    if len(list_of_elements) != elements:
        print("Fewer or more elements are entered than previously specified. Try again")
        quit()
    for el in list_of_elements:
        if el > 20000000000:
            print("One or more of the entered elements exceeds the conditions of the assignment. Try again.")
            quit()
    print("Entered elements") # 15-18, 20 и 21 строки необязательный код, оставлен для наглядности при выполнении задачи
    print(list_of_elements)
    print("Number of entered elements")
    print(len(list_of_elements))
    set_of_elements = set(list_of_elements)
    print("Unique entered elements")
    print(set_of_elements)
    print("Number of unique entered elements")
    print(len(set_of_elements))
