import os
import shutil

# 两个目标文件夹的路径
folder1 = r'D:\koikatsu_2022\abdata\sound\data\pcm\c29\h\wav_voice_success'
folder2 = r'D:\KKVITS'

# 缺失文件复制的目标文件夹
folder_loss = r'D:\KKVITS_LOSS'

# 获取两个文件夹中的文件名
files1 = set(os.listdir(folder1))
files2 = set(os.listdir(folder2))

# 找到只在folder1中存在的文件
only_in_folder1 = files1 - files2

# 复制这些文件到folder_loss
for file_name in only_in_folder1:
    source = os.path.join(folder1, file_name)
    destination = os.path.join(folder_loss, file_name)
    shutil.copyfile(source, destination)
