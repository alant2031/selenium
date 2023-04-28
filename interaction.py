from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys

driver_path = "/home/tnk/tools/geckodriver"
options = webdriver.FirefoxOptions()  # Required as a minimum
service = Service(executable_path=driver_path)
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.python.org/")

learn_more = driver.find_element(By.CLASS_NAME, value="readmore")
donate = driver.find_element(By.LINK_TEXT, "Donate")
search = driver.find_element(By.ID, "id-search-field")

# learn_more.click()
# donate.click()

search.send_keys("selenium")
search.send_keys(Keys.ENTER)
