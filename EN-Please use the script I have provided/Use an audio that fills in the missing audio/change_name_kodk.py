import os
import shutil

# 源文件夹和目标文件夹的路径
source_folder = r'D:\KK_LOSS_DK'
target_folder = r'D:\kk_loss_generated_changename'

# 遍历源文件夹
for filename in os.listdir(source_folder):
    # 如果文件名满足特定的模式
    if filename.startswith('h_ko_dk_29_00_') and filename.endswith('.wav'):
        # 构造新的文件名
        parts = filename.split('_')
        new_filename = 'kodk' + parts[4] + parts[5].split('.')[0] + '.wav'
        # 获取文件的完整原始路径和新路径
        source = os.path.join(source_folder, filename)
        destination = os.path.join(target_folder, new_filename)
        # 复制并重命名文件
        shutil.copyfile(source, destination)
