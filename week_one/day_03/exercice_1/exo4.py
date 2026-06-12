import json


def load_json_and_dump_on_news_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


input_file_path = './data/json/input.json'
output_file_path = './data/json/news.json'
load_json_and_dump_on_news_json(input_file_path)
print(load_json(output_file_path))
