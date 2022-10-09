def get_count_char(str_):
    words =str_.lower().split()
    #words.sort()
    words = ''.join(words)
    char = {}
    DEFAULT_COUNT = 0
    for ch in words:
        if ch.isalpha():
            char[ch] = char.get(ch,DEFAULT_COUNT)+1
    return char

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
