import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', newline='\n') -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
    with open(filename,"r") as f:
        lines = f.readlines()
        headers = lines[0].rstrip().split(delimiter)
        rows = []
        for line in lines[1:]:
            rows.append(line.rstrip().split(delimiter))
        final = []
        for i in range(len(rows)):
            final.append({headers[j]:rows[i][j] for j in range(len(headers))})
    return final

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
