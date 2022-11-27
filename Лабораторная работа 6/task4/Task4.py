import json
INPUT_FILE = "input.csv"

def csv_to_list_dict(INPUT_FILE) -> list[dict]:
    dict_final = []
    dict_rows = []
    with open(INPUT_FILE) as f:
        copy_ = f.readlines()
        headers = copy_[0].rstrip().split(sep = ',')
        for row in copy_[1:]:
            dict_rows.append(row.rstrip().split(sep = ','))

        for i in dict_rows:
            dict_ = {key:value for key,value in zip(headers, i)}
            dict_final.append(dict_)
    return dict_final

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

