from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# #chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# chrome_driver = "chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
# driver.find_elements_by_id("cheddar")
# driver.find_element_by_css_selector("#cheese #cheddar")
# driver.find_elements_by_class_name()
# driver.find_element_by_xpath()
# driver..find_element_by_link_text("新闻")
def 例子():
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 10 , 0.5) #显式等待  until  /  until_not
        driver.implicitly_wait(10) #隐性等待
        driver.get("https://www.baidu.com") #发送请求
        #driver.refresh() #刷新浏览器
        #driver.set_window_size(1400,800) #设置浏览器大小
        driver.maximize_window()   #浏览器窗口最大化
        driver.find_element_by_id("kw").send_keys("selenium",Keys.ENTER)
        #driver.find_element_by_id("su").click()
        time.sleep(10)
        first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
        #print(first_result.get_attribute("textContent"))
def 综合():
    #先快捷方式后加' --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"  https://live.bwjf.com/dashboard'打开浏览器
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    driver.implicitly_wait(10)

    def 点击按钮(按钮位置):
        time.sleep(0.2)
        driver.find_element_by_xpath(按钮位置).click()
    def 填写内容(按钮位置,内容):
        driver.find_element_by_xpath(按钮位置).send_keys(内容)
    def 选择下拉框(按钮位置,选项):
        点击按钮(按钮位置)
        time.sleep(0.1)
        点击选项 = driver.find_element_by_xpath('''//span[text()="'''+选项+'''"]''')
        print(点击选项)
        点击选项.click()
    def 选择下拉框特殊(按钮位置,选项):
        点击按钮(按钮位置)
        time.sleep(0.1)
        点击选项 = driver.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item:nth-child(2)')
        点击选项.click()
    def 输入后选择下拉框(按钮位置,内容和选项):
        填写内容(按钮位置,内容和选项)
        print('''//span[text()="'''+内容和选项+'''"]''')
        time.sleep(0.1)
        选项出现 = driver.find_element_by_xpath('''//span[text()="'''+内容和选项+'''"]''')
        time.sleep(0.5)
        选项出现.click()


import os,sys,django,xlrd
# 本文件在manage.py同文件夹下
def django导入库数据():
    文件名 = '表.xls'
    读取的Excel = xlrd.open_workbook(filename = 文件名)
    文件内第一个表= 读取的Excel.sheet_by_index(0)
    # def 获得列序号(表名,查找字段名):
    #     列序号 = None
    #     for i in range(表名.ncols):
    #         if (表名.cell_value(0,i) == 查找字段名):
    #             列序号 = i
    #             break
    #     return 列序号
    #竖向资料 = [文件内第一个表.col_values(i) for i in range(文件内第一个表.ncols)]
    横向资料 = [文件内第一个表.row_values(i) for i in range(1,文件内第一个表.nrows)]

    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'shuai.settings'
    django.setup()
    from APP名称.models import 模型类名
    list = []
    for i in 横向资料:
        list.append(模型类名(字段1 = i[0],字段2 = i[1],字段3 = i[2],字段4 = i[3]))

    模型类名.objects.bulk_create(list)


