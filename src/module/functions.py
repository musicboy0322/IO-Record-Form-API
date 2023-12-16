import secrets
import string
import json

def yield_random_identifier():
    characters = string.ascii_lowercase + string.digits
    identifier = ''
    for i in range(10):
        identifier += secrets.choice(characters)
    return identifier

def change_to_json(data):
    result_list = list(data)
    json_data = json.dumps(result_list,ensure_ascii=False)
    return json_data

def split_amount_result(data):
    split = int(data.split(',')[0].split('(')[2])
    return split

def split_total_amount(data):
    split = int(data.split("'")[1].split("'")[0])
    return split

def split_vertification_result(data):
    split = int(data.split(',')[0].split('(')[2])
    return split