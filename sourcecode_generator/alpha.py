import os
import shutil
import unittest
from shutil import copyfile

# 遍历存放java源文件转成的txt文件的文件夹
# 第二个参数为目标TXT文件
from sourcecode_generator import txtConverter
from sourcecode_generator.sourcecodeInjector import traverse_txt_dir
from sourcecode_generator.txtConverter import TxtConverter


# 一切齐活儿后，删除txt文件的文件夹
def del_txt_dir(dir_path):
    shutil.rmtree(dir_path)


def convert_to_txt2(file_full_path, dst_dir):
    paths = file_full_path.split("\\")
    file_name = paths[-1]
    file_dir = file_full_path.replace('\\' + file_name, '')

    names = os.path.splitext(file_name)
    new_name = names[0] + '.txt'
    os.rename(os.path.join(file_dir, file_name), os.path.join(dst_dir, new_name))


class MyTestCase(unittest.TestCase):

    def test_step1(self):
        project_path = r"C:\Users\Administrator\Desktop\宗师周神\工作资料\第五视觉\验收2cond\后端\backend"
        converter = TxtConverter()
        converter.traverse_project(project_path, '.java', r'E:\test')
        self.assertEqual(1, 1)

    def test_step2(self):
        traverse_txt_dir(r'E:\test', r'E:\copyright\sourcecode.txt')
        self.assertEqual(1, 1)

    def test_step1_and_2(self):
        project_path = r"C:\Users\Administrator\Desktop\宗师周神\工作资料\第五视觉\验收2cond\前端\frontend"
        txt_dir_path = r'E:\copyright\temp'
        sourcecode_file = r'E:\copyright\sourcecode.txt'
        suffix = r'.vue'

        converter = TxtConverter()
        converter.traverse_project(project_path, suffix, txt_dir_path)

        traverse_txt_dir(txt_dir_path, sourcecode_file)
        self.assertEqual(1, 1)

    def test_del_blank_line(self):
        input_file = r'E:\copyright\sourcecode.txt'
        output_file = r'E:\copyright\sourcecode2.txt'
        outfile = open(output_file, mode='a', encoding='utf-8')

        with open(input_file, mode='r', encoding='utf-8') as infile:
            while True:
                line = infile.readline()
                if line.strip() and line.find('@author') == -1 and line.find('@Author') == -1 and line.find(
                        '@date') == -1 and line.find('@Date') == -1 and line.find('*') == -1:
                    outfile.writelines(line)
                if not line:
                    break

        outfile.close()
        self.assertEqual(1, 1)

    def test_del_date_author_line(self):
        self.assertEqual(1, 1)

    def test_weier(self):
        file_path = r"E:\copyright\sheshe.txt"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        sourcecode_file = open(file_path, mode='ab')
        sourcecode_file.close()
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
