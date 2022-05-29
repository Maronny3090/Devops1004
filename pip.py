#pip install selenium

from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="C:/Users/Ronny/Downloads/chromedriver_win32/chromedriver.exe")

my_driver.get("C:/Users/Ronny/Downloads/tip_calc/index.html")
my_driver.find_element_by_id()
my_driver.find_element_by_xpath()
