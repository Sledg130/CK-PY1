import json
INPUT_FILE = "input.csv"


def csv_to_list_dict(filenames, delimiter = ',', new_line = '\n') -> list[dict]:
    list_dik = []
    list_rows = []
    with open(filenames, 'r', encoding='utf8') as f:
        result = f.readlines()
        headers = result[0].rstrip(new_line).split(delimiter)
        for row in result[1:]:
            list_rows.append(row.rstrip(new_line).split(delimiter))

        for element in list_rows:
            dict_ = {key:value for key,value in zip(headers, element)}
            list_dik.append(dict_)
    return list_dik

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

