# TODO импортировать необходимые молули
from csv import DictReader
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME,"r") as f:
        list_of_dict = [row for row in DictReader(f)] # TODO считать содержимое csv файла
    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(list_of_dict,f,indent=4)
    ...  # TODO записать список словарей в json файл


task()

with open(OUTPUT_FILENAME) as output_f:
    for line in output_f:
        print(line, end="")
