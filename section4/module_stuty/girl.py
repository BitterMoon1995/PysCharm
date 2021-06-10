a = 100


def wear_jk() -> None:
    print('girl模块函数：女生穿JK')


"""
__name__是python的一个内置类属性，它存储模块的名称。
python的模块既可以被调用，也可以独立运行。而被调用时__name__存储的是py文件名(模块名称)，独立运行时存储的是"__main__"。
那么它的作用主要就是用来区分，当前模块是独立运行还是被调用。
"""
if __name__ == '__main__':
    print('模块自身运行')
# 被其他模块引入（指一旦出现import girl）时就会走这个分支，引入时被取了别名也不影响
elif __name__ == 'girl':
    print('girl模块被引入')
