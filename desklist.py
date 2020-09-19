import win32gui,win32con,win32api

# 操作win32相关
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


import json
import requests
def 爬虫获取post数据():
    #登陆url = 'user/login'
    postUrl = ''
    # payloadData数据
    payloadData = {
    '': ""
        }

    # data={
    #     '': "",
    #     '': "",
    # }

    # 请求头设置
    payloadHeader = {
    'Host': '',
    'Origin': '',
    #'Cookie': '',
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Content-Type': 'application/json',
    'Content-Length': '32',
    'Connection': 'keep-alive',
    'Authorization': 'bearer eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDE1OTQ4NjAsInN1YiI6ImJ3eWRiZyJ9.t_XDqE2CaCSxg_Mtw5BrgUCTFpjpmU9oyI32oGPO9wY',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'application/json, text/plain, */*',
    }
	# 下载超时
    timeOut = 25
    #session=requests.session()
    #session.post(登陆url,headers=payloadHeader,data=data)
    #r = requests.post(postUrl, data=json.dumps(payloadData), headers=payloadHeader)
    dumpJsonData = json.dumps(payloadData)
    #res = session.post(postUrl, data=dumpJsonData, headers=payloadHeader, timeout=timeOut, allow_redirects=False)
    res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader, timeout=timeOut, allow_redirects=False)
    # 下面这种直接填充json参数的方式也OK
    # res = requests.post(postUrl, json=payloadData, headers=header)
    #print(f"responseTime = {datetime.datetime.now()}, statusCode = {res.status_code}, res text = {res.text}")
    res_dict = eval(res.text)
    信息列表 = []
    for i in res_dict['obj']:
        信息列表.append(i['khmc']+'--')
    return 信息列表
