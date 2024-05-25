import json
from pathlib import Path 

def file_path(file):
    return Path(__file__).resolve().parent / file

class file_handle:
    def file_reading(self, file:str, key:str):
        json_file_path_reading = file_path(file)
        with json_file_path_reading.open("r", encoding="utf-8") as json_file:  
            loaded_data = json.load(json_file)  
            return loaded_data[key]  