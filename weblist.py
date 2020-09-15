from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# browser.maximize_window()   #浏览器窗口最大化
# browser.get('http://www.baidu.com/')

#打开浏览器()4844
chrome_options = Options()
#chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.get('http://www.baidu.com/')
driver.implicitly_wait(10)
