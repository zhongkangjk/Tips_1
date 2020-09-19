# -*- coding:utf-8 -*-
import tkinter,sys,os
import webbrowser
import requests
from lxml import etree
#资料引入
def resource_path(relative_path):
    '''返回资源绝对路径。'''
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller会创建临时文件夹temp
        # 并把路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)
logo = resource_path('1.ico')
def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
            "cookie":"hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; enc=sjA56zcJ9u%2F8HHfzWeGenkosE0sTJKOlrlE3PMUsXa4T4ucIGh7utUvQoTVW1UqNtT0z0zaGdAm6xBhWgTSwhQ%3D%3D; miid=202266272065909521; tracknick=zhongkangtb; _cc_=U%2BGCWk%2F7og%3D%3D; tg=0; cna=Q8BkEwdNjwACASrHh4ywLeIq; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; t=495b1ae6d656f25318235b91cf412b1a; cookie2=1e352b66734f3c1b206751d815d354ed; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _tb_token_=e53945567abe7; mt=ci%3D-1_1; JSESSIONID=694C8BC65EFD5DCBCB5BD0FFFF0A8D54; isg=BOXl0kSA1LkPtzG_hnKhESi05qHfioaHPErXpufJqJwr_gRwr3FyhCfciCItfrFs; l=cBIvTKdVvmfdhDbzBOfZVuI81hQtoQ908sPzw4swkICP9wCH50UfWZeIGwLMCnGVK6SDR3Sq8BObB0LNuyCqJxpsw3k_J_f.."
        }
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取失败")
        #'http://poedb.tw/tw/unique.php?n=Hands_of_the_High_Templar'
def 标准联盟(url):
    html = etree.HTML(getHTMLText(url))
    res = html.xpath("/html/body/div[5]/div/table[2]/tbody//tr//td[1]/text()")
    价格 = [i for i in res]
    res1 = html.xpath("/html/body/div[5]/div/table[2]/tbody//tr//td[2]/text()")
    数量= [i for i in res1]
    标准 = [[价格[i],数量[i]] for i in range(len(价格))]
    return 标准
def 赛季联盟(url):
    html = etree.HTML(getHTMLText(url))
    res3 = html.xpath("/html/body/div[5]/div/table[3]/tbody//tr//td[1]/text()")
    价格1 = [i for i in res3]
    res4 = html.xpath("/html/body/div[5]/div/table[3]/tbody//tr//td[2]/text()")
    数量1= [i for i in res4]
    赛季 = [[价格1[i],数量1[i]] for i in range(len(价格1))]
    return 赛季
list1 = [{'ch_name': '北方雷霆聖杖', 'en_name': 'Agnerod North'},]  #映射文件
def 获得url():
    r = tkinter.Tk()
    r.withdraw()
    try:
        st = r.clipboard_get().split('\n')[1]
        for i in list1:
            if st == i["ch_name"]:
                name = st
                url = f'http://poedb.tw/tw/unique.php?n={i["en_name"]}'
                #text1.delete(0.0, tkinter.END)
                #text1.insert(tkinter.INSERT, "OK正在打开网页")
                #webbrowser.open(url)
                res = [name,url]
                return res
        else:
            text1.delete(0.0, tkinter.END)
            text1.insert(tkinter.INSERT, "我居然没有找到这件传奇")
    except:
        text1.delete(0.0, tkinter.END)
        text1.insert(tkinter.INSERT, "你复制这个东西似乎有点问题啊")
'''

西里的戰衣
聖宗神手
'''
def 显示价格():
    name = 获得url()[0]
    text1.delete(0.0, tkinter.END)
    text1.insert(tkinter.INSERT, name +'\n')
    text1.insert(tkinter.INSERT, '\r\n标准联盟'+'\n')
    for i in 标准联盟(获得url()[1]):
        text1.insert(tkinter.INSERT, "%-15s %-5s \n"%(i[0],i[1]))
    text1.insert(tkinter.INSERT, '\r\n赛季联盟'+'\n')
    for j in 赛季联盟(获得url()[1]):
        text1.insert(tkinter.INSERT, "%-15s %-5s \n"%(j[0],j[1]))

def 打开网页():
    text1.delete(0.0, tkinter.END)
    text1.insert(tkinter.INSERT, "OK正在打开网页")
    webbrowser.open(获得url()[1])

win = tkinter.Tk()
win.iconbitmap(logo)
win.title("挖挖")
win.geometry('180x400+900+300')
win.resizable(0, 0)
tkinter.Button(win,text = "显示价格",command = 显示价格).pack(fill='both')
text1 = tkinter.Text(win,width=59,height=26)
text1.pack()
tkinter.Button(win,text = "打开网页链接",command = 打开网页).pack(fill='both')
win.mainloop()