from random import randint


def get_unique_list_numbers() -> list[int]:
    list_of_numbers = []    # TODO написать функцию для получения списка уникальных целых чисел
    while len(list_of_numbers) < 15:
        a = randint(-10,10)
        if a not in list_of_numbers:
            list_of_numbers.append(a)
    return list_of_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
