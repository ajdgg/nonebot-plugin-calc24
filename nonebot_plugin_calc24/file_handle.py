import json
from pathlib import Path


def file_path(file):
    return Path(__file__).resolve().parent / file


class file_handle:
    def file_reading(self, file: str, key: str):
        json_file_path_reading = file_path(file)
        with json_file_path_reading.open("r", encoding="utf-8") as json_file:
            loaded_data = json.load(json_file)
            return loaded_data[key]

    def file_change(self, file: str, key: str, value: str):
        json_file_path_change = file_path(file)
        with json_file_path_change.open('r', encoding='utf-8') as f:
            data = json.load(f)
        data[key] = value
        with json_file_path_change.open('w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
