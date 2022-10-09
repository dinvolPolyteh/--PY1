# TODO реализовать функцию
def remove_whitespace(sentence):
    i = 1
    while i < len(sentence):
        if sentence[i] == sentence[i-1] and sentence[i-1] == " ":
            sentence = sentence[:i] + sentence[i+1:]
        else:
            i+=1
    return sentence
str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
