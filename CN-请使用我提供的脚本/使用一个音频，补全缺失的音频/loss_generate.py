import os
import shutil

# 音频源文件的路径
source_file = r'C:\Users\Skywalker\Desktop\新建文件夹\ko00502.wav'

# 目标文件夹的路径
folder = r'D:\KKVITS_LOSS'
target_folder = r'D:\KK_LOSS_GENERATE'

# 遍历目标文件夹
for filename in os.listdir(folder):
    # 创建新的文件名，其路径为目标文件夹中的文件名
    new_filename = os.path.join(target_folder, filename)
    # 复制源文件到新的文件名
    shutil.copyfile(source_file, new_filename)
