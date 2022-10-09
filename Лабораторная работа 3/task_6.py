list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

i = 0
max_el = -10**16
index = i
while i < len(list_numbers)-1:
    if list_numbers[i] > max_el:
        max_el = list_numbers[i]
        index = i
    i+=1

list_numbers[index] = list_numbers[len(list_numbers)-1]
list_numbers[len(list_numbers)-1] = max_el
print(list_numbers)
