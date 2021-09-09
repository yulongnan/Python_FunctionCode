# 复制文件夹到另一个文件夹   


import shutil, os, collections,time,zipfile

def copyDir(sourcePath, targetPath):
    if not os.path.isdir(sourcePath):
        return '源目录不存在'
    # 创建两个栈,一个用来存放原目录路径,另一个用来存放需要复制的目标目录
    sourceStack = collections.deque()
    sourceStack.append(sourcePath)
    targetStack = collections.deque()
    targetStack.append(targetPath)
    # 创建一个循环当栈里面位空时结束循环
    while True:
        if len(sourceStack) == 0:
            break
        # 将路径从栈的上部取出
        sourcePath = sourceStack.pop()  # sourcePath = sourceStack.popleft()
        # 遍历出该目录下的所有文件和目录
        listName = os.listdir(sourcePath)

        # 将目录路径取出来
        targetPath = targetStack.pop()  # targetPath = targetStack.popleft()
        # 判断该目标目录是否存在,如果不存在就创建
        if not os.path.isdir(targetPath):
            os.makedirs(targetPath)
        # 遍历目录下所有文件组成的列表,判断是文件,还是目录
        for name in listName:
            # 拼接新的路径
            sourceAbs = os.path.join(sourcePath, name)
            targetAbs = os.path.join(targetPath, name)
            # 判断是否时目录
            if os.path.isdir(sourceAbs):
                # 判断目标路径是否存在,如果不存在就创建一个
                if not os.path.exists(targetAbs):
                    os.makedirs(targetAbs)
                # 将新的目录添加到栈的顶部
                sourceStack.append(sourceAbs)
                targetStack.append(targetAbs)
            # 判断是否是文件
            if os.path.isfile(sourceAbs):
                shutil.copyfile(sourceAbs,targetAbs)
  
# 使用
source_path = './logs'   
target_path = '../L'   
copyDir(source_path, target_path)   
