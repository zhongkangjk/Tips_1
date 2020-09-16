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


