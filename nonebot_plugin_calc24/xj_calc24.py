import re
import json
import random
import os

# 加载无效数据列表
script_path = os.path.abspath(__file__)
current_dir = os.path.dirname(script_path)
json_file_path = os.path.join(current_dir, "calc24_invalid_data.json")


with open(json_file_path, "r") as json_file:
    loaded_data = json.load(json_file)
    legal_data_array = loaded_data["data"]
new_continuous_legal_data = {tuple(arr): None for arr in legal_data_array}

def check_if_in_dict(array):
    key_tuple = tuple(array)
    return key_tuple in new_continuous_legal_data

# 生成随机数函数
def random_number_generator():
    intdata = [1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6, 7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10, 11,11,11,11, 12,12,12,12, 13,13,13,13]
    a_data = random.sample(intdata, 4)
    # a_data = [1,1,1,1]
    if check_if_in_dict(a_data):
        return random.sample(intdata, 4) 
    return a_data

def paixu(sort_array):
        return sorted(sort_array, reverse=True)

class xj_calc24:
    def a_main(self):
        return random_number_generator()
    
    


    def b_main(self, equation, array):
        numbers_str = re.findall(r'\d+', equation)
        # 将匹配到的数字字符串转换为整数数组
        numbers_int = [int(num) for num in numbers_str]
        # print("csaa",numbers_int)
        if paixu(numbers_int) != paixu(array):
            return 'no'
    
        if eval(equation) == 24:
            return '傻逼你居然答对了'
        return '傻逼我'