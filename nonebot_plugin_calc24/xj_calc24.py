import re
import random
from .file_handle import file_handle

file_handle = file_handle()

legal_data_array = file_handle.file_reading("calc24-data.json", "data")
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

def regular_expression(regular , string):
    matching_result = re.findall(regular, string)
    if matching_result:
        return True
    return False


class xj_calc24:
    def calc_a_main(self):
        return random_number_generator()

    def calc_b_main(self, equation, array):

        regular_a = r'(?:[+\-*/]{2})'
        if regular_expression(regular_a, equation):
            return 'CONTINUOUS_OPERATOR'

        plain_english_text = equation.replace('（', '(').replace('）', ')')
        numbers_str = re.findall(r'\d+', plain_english_text)
        numbers_int = [int(num) for num in numbers_str]
        # print("csaa",numbers_int)
        if paixu(numbers_int) != paixu(array):
            return 'NO'
    
        if eval(plain_english_text) == 24:
            return
        return 'ERROR'
