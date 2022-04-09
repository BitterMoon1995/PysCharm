import os
import shutil


# 遍历存放转换为txt的代码文件的文件夹，遍历所以txt代码文件
def traverse_txt_dir(txt_dir_path, dst_file_path):
    for path, dirs, files in os.walk(txt_dir_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(path, file)
                write_to_dst_file(file_path, dst_file_path)
    shutil.rmtree(txt_dir_path)


# 源TXT文件追加写入目标TXT文件
def write_to_dst_file(src_file_path, dst_file_path):
    # 如果目标TXT文件不存在则创建
    if not os.path.exists(dst_file_path):
        os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
        code_file = open(dst_file_path, mode='ab')
        code_file.close()

    src_file = open(src_file_path, 'rb')
    with open(dst_file_path, mode='ab') as dst_file:
        while True:
            line = src_file.readline()
            dst_file.write(src_file.readline())
            if not line:
                break
    src_file.close()
