import os

# 目标文件夹的路径
folder = r'D:\koikatsu_2022\abdata\sound\data\pcm\c29\h\wav_voice_success'

# 遍历文件夹
for filename in os.listdir(folder):
    # 如果文件名以'_0.wav'结尾
    if filename.endswith('_0.wav'):
        # 构造新的文件名
        new_filename = filename[:-6] + '.wav'
        # 获取文件的完整原始路径和新路径
        source = os.path.join(folder, filename)
        destination = os.path.join(folder, new_filename)
        # 重命名文件
        os.rename(source, destination)
