from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    count_eagle = 0
    for i in range(count):
        if choice(coin) == EAGLE:
            count_eagle +=1# TODO подсчитать количество выпаданий орлов и решек
    list_freq.append(min(count_eagle,count-count_eagle)/max(count_eagle,count-count_eagle))
    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

print(list_freq)
