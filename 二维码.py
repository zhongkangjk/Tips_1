#嫖群友的二维码生成
import qrcode
import tkinter as tk 
from tkinter import filedialog 
import os 

window = tk.Tk() 
window.title('窗口标题') # 标题
window.geometry('500x500') 
# 窗口尺寸 
file_path = '' 
file_text = '' 
text1 = tk.Text(window, width=50, height=20, bg='orange', font=('Arial', 12)) 
text1.pack() 
def open_file(): 
    ''' 打开文件 :return: ''' 
    global file_path 
    global file_text 
    file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/'))) 
    print('打开文件：', file_path) 
    if file_path is not None: 
        with open(file=file_path, mode='r+', encoding='utf-8') as file: 
            file_text = file.read() 
            text1.insert('insert', file_text) 
def save_file(): 
    global file_text 
    qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=10, border=2, ) # 设置图片格式 
    qr.add_data(file_text) 
    qr.make(fit=True) 
    img = qr.make_image() 
    img.save('D:/simpleqrcode.jpg') 
    img.show() 
    window.quit() 
bt1 = tk.Button(window, text='打开文件', width=15, height=2, command=open_file) 
bt1.pack() 
bt2 = tk.Button(window, text='确认生成二维码', width=15, height=2, command=save_file) 
bt2.pack() 
window.mainloop() # 显示


