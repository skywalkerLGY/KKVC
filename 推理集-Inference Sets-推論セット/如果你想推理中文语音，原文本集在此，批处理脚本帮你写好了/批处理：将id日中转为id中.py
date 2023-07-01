import re
from zhon import zh


# 输入文件路径
input_file_path = r'C:\Users\Skywalker\Desktop\碧蓝档案\推理集\c38几帐面.txt'

# 输出文件路径
output_file_path = r'C:\Users\Skywalker\Desktop\碧蓝档案\推理集1\c38几帐面_output.txt'


# 打开文件
with open(input_file_path, 'r', encoding='utf-8') as in_file, \
     open(output_file_path, 'w', encoding='utf-8') as out_file:
    for line in in_file:
        # 使用正则表达式找到id和中文
        match = re.match(fr'(\S+)\s+([{zh.characters}]+)\s+', line)
        if match:
            # 获取id和中文
            id_, chinese = match.groups()
            # 将id和中文用'|'连接并写入新文件
            out_file.write(f'{id_}|{chinese}\n')
