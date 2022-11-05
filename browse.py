from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=~/.chrome_driver_session')
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

target = 'Regy'
string = 'Hi'

driver.get('http://web.whatsapp.com')

# Click to search chat
img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]')))
searchBar = driver.find_element(by='xpath', value='//*[@id="side"]/div[1]/div/div/div[2]')
searchBar.click()

# # Type to find specific chat
focused_elem = driver.switch_to.active_element
focused_elem.send_keys("It's Operation Time!")

# Click the chat room




