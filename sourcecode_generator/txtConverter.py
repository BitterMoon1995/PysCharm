import dataclasses
import os
from shutil import copyfile


class TxtConverter:
    repeat_count = 0

    # 遍历项目中所有扩展名为ext_name的文件
    def traverse_project(self, project_path, ext_name, txt_dir_path):
        if not os.path.exists(txt_dir_path):
            # 用这个不要用mkdir，这个才能递归创建
            os.makedirs(txt_dir_path, exist_ok=True)

        for path, dirs, files in os.walk(project_path):
            for file in files:
                if file.endswith(ext_name):
                    print(os.path.join(path, file))
                    self.convert_to_txt(file, path, txt_dir_path)

    # 代码源文件转换为指定目录下的同名txt文件
    def convert_to_txt(self, file_name, file_path, txt_dir_path):
        stem, suffix = os.path.splitext(file_name)
        new_name = stem + '.txt'

        src_file = os.path.join(file_path, file_name)
        copy_file = os.path.join(txt_dir_path, 't-' + file_name)

        # 只要一个流程完整执行，拷贝的中间文件就不会存在，所以不能作为去重判断条件
        rename_file = os.path.join(txt_dir_path, new_name)
        if os.path.exists(rename_file):
            # 允许文件名重复的处理方式
            # rename_file = os.path.join(txt_dir_path, new_name + '-' + str(self.repeat_count))
            # self.repeat_count += 1
            return

        # 先拷贝一份到模板文件夹，不要直接重命名源文件，因为源文件会消失
        copyfile(src_file, copy_file)

        # if os.path.exists(rename_file):

        os.rename(copy_file, rename_file)
