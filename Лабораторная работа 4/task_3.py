def delete(list_, index=None):
    if index == None or index >= len(list_)-1:# TODO реализовать функцию удаления элемента из списка по индексу
        list_ = list_[:len(list_)-1]
    else:
        list_1 = list_[:index]
        list_2 = list_[index+1:]
        list_ = list_1 + list_2
    return list_

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
