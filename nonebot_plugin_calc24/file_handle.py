from pathlib import Path
import json


def file_path(file):
    return Path(__file__).resolve().parent / file


class file_handle:
    def file_reading(self, file: str, key: str):
        try:
            json_file_path_reading = file_path(file)
            with json_file_path_reading.open("r", encoding="utf-8") as json_file:
                loaded_data = json.load(json_file)
                return loaded_data.get(key, None)
        except FileNotFoundError:
            print(f"File not found: {file}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file: {file}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def file_change(self, file: str, key: str, value: str):
        try:
            json_file_path_change = file_path(file)
            with json_file_path_change.open('r', encoding='utf-8') as f:
                data = json.load(f)
            data[key] = value
            with json_file_path_change.open('w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print(f"File not found: {file}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file: {file}")
        except Exception as e:
            print(f"An error occurred when writing to the file: {e}")
