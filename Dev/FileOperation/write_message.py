# 将文本写入到文件中去
filepath = 'text_files//programming.txt'
with open(filepath, 'w') as file_object:
    file_object.write('I love you\n')
    file_object.write('I love you too\n')
