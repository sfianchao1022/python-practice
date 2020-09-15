# 嵌入其他python檔案 模組化程式
import function  # 也會執行function.py
from function import kg_to_lbs  # 可以直接使用function內的函式
from function import lbs_to_kg

my_weight_lbs = function.kg_to_lbs(80)
print(my_weight_lbs)
my_weight_kg = function.lbs_to_kg(180)
print(my_weight_kg)

print(kg_to_lbs(90))
print(lbs_to_kg(150))

from function import find_max

result = find_max([3, 4, 60, 34, 45, 435])
print(result)
print(max([34, 456, 53, 343, 999]))  # python 內建max函式