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