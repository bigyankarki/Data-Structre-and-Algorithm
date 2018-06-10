myList = [12,55,67,99,12,1,4,6]


def seq_search(lst, item):
    found = False
    for element in lst:
        if element == item:
            found = True
    return found


print(seq_search(myList, 122))