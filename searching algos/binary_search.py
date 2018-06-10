myList = [12,55,67,99,12,1,4,6]


# Without using recursion.
def binary_search(lst, item):
    lst.sort()

    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if lst[middle] == item:
            found = True
        elif item < lst[middle]:
            last = middle - 1
        elif item > lst[middle]:
            first = middle + 1

    return found

print(binary_search(myList, 4))
print(binary_search(myList, 25))


# using recursion
def recur_binary_search(lst, item):
    lst.sort()

    if len(lst) == 0:
        return False
    else:
        middle = len(lst) // 2
        if item == lst[middle]:
            return True
        elif item < lst[middle]:
            return recur_binary_search(lst[:middle], item)
        else:
            return recur_binary_search(lst[middle+1:], item)


print(recur_binary_search(myList, 4))
print(recur_binary_search(myList, 25))

