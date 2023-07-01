import os
import shutil

def rename_file(old_name):
    # 分解旧文件名
    split_name = old_name.split('_')
    new_name = ''

    if len(split_name) == 6: # 对于有6个部分的文件名
        if split_name[4] == '00':
            new_name = f"{split_name[1]}dk{split_name[5]}"
        else:
            new_name = f"{split_name[1]}{split_name[3]}{split_name[4]}{split_name[5]}"

    elif len(split_name) == 5: # 对于有5个部分的文件名
        new_name = f"{split_name[1]}{split_name[3]}{split_name[4]}"

    return new_name

# 指定源目录和目标目录
src_dir = r'D:\KK_LOSS_GENERATE'
dst_dir = r'D:\kk_loss_generated_changename'

# 遍历源目录下的所有文件
for file_name in os.listdir(src_dir):
    # 获得完整的文件路径
    src_file = os.path.join(src_dir, file_name)
    
    # 跳过非 .wav 文件
    if not src_file.endswith('.wav'):
        continue

    # 获取新的文件名
    new_name = rename_file(os.path.splitext(file_name)[0])
    if new_name: # 如果新名称非空
        new_name += '.wav' # 添加文件扩展名
        dst_file = os.path.join(dst_dir, new_name)

        # 复制并重命名文件
        shutil.copy2(src_file, dst_file)

    else: # 如果新名称为空（即原文件名不符合要求）
        print(f"Skipping file: {src_file} due to invalid name format.")
