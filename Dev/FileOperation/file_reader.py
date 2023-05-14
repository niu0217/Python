# 简单读取txt文件内容并打印出来
with open('text_files/learning_python.txt', 'r', encoding='ISO8859-1') as file_object:
    lines = file_object.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.replace('Python', 'C++')  # 将文件中的Python替换成C++
        print(line)
