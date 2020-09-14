import os,sys



def 返回文件绝对路径(当前路径文件名):
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller会创建临时文件夹temp
        # 并把路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, 当前路径文件名)

print(返回文件绝对路径('list1.py'))