import os
import subprocess

# 指定文件夹路径
folder_path = r'D:\koikatsu_2022\abdata\sound\data\pcm\c29\h\voice'
# 指定转换工具路径
conversion_tool = r'D:\koikatsu_2022\abdata\sound\data\pcm\c29\h\543\fsb提取工具\fmod_extr.exe'

# 遍历文件夹
for filename in os.listdir(folder_path):
    # 检查文件扩展名是否为FSB
    if filename.endswith('.fsb'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)
        
        # 构建转换命令
        command = [conversion_tool, file_path]
        
        try:
            # 执行转换命令
            subprocess.run(command, shell=True, check=True)
            print(f"转换成功：{filename}")
        except subprocess.CalledProcessError as e:
            print(f"转换失败：{filename}，错误信息：{e}")
