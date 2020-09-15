import os,sys

def 返回文件绝对路径(当前路径文件名):
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller会创建临时文件夹temp
        # 并把路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, 当前路径文件名)

#print(返回文件绝对路径('list1.py'))


import os

def 返回当前路径第一个包含名字的文件(名字):
    namelist = os.listdir(os.getcwd())
    for x in namelist:
        if 名字 in x and '$' not in x:
            路径 = x
            return 路径
            break
#print(返回当前路径第一个包含名字的文件('lis'))


import xlrd

class 打开excel文件():
    def __init__(self,文件名,第几个表):
        self.文件 = xlrd.open_workbook(filename = 文件名)
        self.表 = self.文件.sheet_by_index(第几个表-1)


    def 获得横向资料(self):
        self.数据 = [self.表.row_values(i) for i in range(self.表.nrows)]
        return self.数据


    def 获得纵向资料(self):
        self.数据 =  [self.表.col_values(i) for i in range(self.表.ncols)]
        return self.数据

    def 获得名称列数据(self,名称):
        def 获得列序号(表名,查找字段名):
            列序号 = None
            for i in range(表名.ncols):
                if (表名.cell_value(0,i) == 查找字段名):
                    列序号 = i
                    break
            return 列序号
        print(获得列序号(self.表,名称))
        self.数据 = self.表.col_values(获得列序号(self.表,名称),2)
        return self.数据

# 文件 = 打开excel文件('测试.xlsx',1)
# print(文件.获得名称列数据('地址'))


import win32gui,win32con,win32api

def 点击(id):
	win32gui.SendMessage(id,win32con.WM_LBUTTONDOWN, 0,0)
	win32gui.PostMessage(id,win32con.WM_LBUTTONUP, 0,0)
def 填信息(id,text):
	win32gui.SendMessage(id,win32con.WM_SETTEXT, 0,text)
def 发送回车(id):
    win32gui.SendMessage(id,win32con.WM_KEYDOWN, win32con.VK_RETURN,0)
    win32gui.PostMessage(id,win32con.WM_KEYUP, win32con.VK_RETURN,0)
def 列出子窗口句柄(id):
	hwndChildList = []
	win32gui.EnumChildWindows(id, lambda hwnd,param: param.append(hwnd),hwndChildList)
	n = 0
	for i in hwndChildList:
		print(i ,"{:#016X}".format(i),win32gui.GetWindowText(i),n)
		n += 1
	return hwndChildList
def 获得窗口标题的句柄(name):
    hwndChildList = []
    win32gui.EnumChildWindows(None, lambda hwnd,param: param.append(hwnd),hwndChildList)
    for i in hwndChildList:
        if name in win32gui.GetWindowText(i):
            return i
def 提取句柄文本(句柄):
	# 获取识别结果中输入框文本
	length = win32gui.SendMessage(句柄, win32con.WM_GETTEXTLENGTH)+1
	buf = win32gui.PyMakeBuffer(length)
	#发送获取文本请求
	win32api.SendMessage(句柄, win32con.WM_GETTEXT, length, buf)
	#下面应该是将内存读取文本
	address, length = win32gui.PyGetBufferAddressAndLen(buf[:-1])
	text = win32gui.PyGetString(address, length)
	return text
#print(提取句柄文本(列出子窗口句柄(获得窗口标题的句柄('来电接听'))[41]))


from tkinter import *
from tkinter import ttk
def 连续点击tkinter():
    表1 = [1,2,3]
    表2 = [4,5,6]
    表3 = [7,8,9]
    表 = [表1,表2,表3]
        
    def 选表():
        players["values"] = 表[var.get()-1]
        players.current(0) #默认第一个开始
    def 执行查找(*args):
        #使用players.get()
        #然后自增
        players.set(players["values"][players["values"].index(players.get())+1])
    root = Tk()
    var = IntVar()
    var.set(1)
    name = StringVar()
    root.wm_attributes('-topmost',1)

    单选框1 = Radiobutton(root, text="表1", value=1, variable=var, command = 选表).pack()
    单选框2 = Radiobutton(root, text="表2", value=2, variable=var, command = 选表).pack()
    单选框2 = Radiobutton(root, text="表3", value=3, variable=var, command = 选表).pack()

    players = ttk.Combobox(root, textvariable=name,width=50)
    players["values"] = 表1
    players["state"] = "readonly"
    
    players.current(0)
    # players.set("演员表")
    # print(players.get())

    players.pack()
    Button(root,text = "点击查询",command = 执行查找,width=50,height=20).pack()

    root.mainloop()