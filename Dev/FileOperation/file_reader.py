# 简单读取txt文件
with open('Data/pi_digits.txt', 'r', encoding='ISO8859-1') as file_object:
    contents = file_object.read()
    print(contents)

