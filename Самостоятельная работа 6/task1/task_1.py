import json

# TODO решите задачу
def task() -> float:
    with open("input.json") as f:
        list_of_dic = json.load(f)
    return round(sum(item["score"]*item["weight"] for item in list_of_dic),3)

print(task())
