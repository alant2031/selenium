from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

driver_path = "/home/tnk/tools/geckodriver"
options = webdriver.FirefoxOptions()  # Required as a minimum
service = Service(executable_path=driver_path)
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://pt.wikipedia.org")

main_article = driver.find_element(
    By.CSS_SELECTOR, "div.main-page-block-heading"
)
search = driver.find_element(By.NAME, "search")
bug_link = driver.find_element(
    By.XPATH,
    '//*[@id="mw-content-text"]/div[1]/div[1]/div/div[1]/table/tbody/tr/td[2]/div/ul/li[4]/a',
)


print(main_article.text)
print(search.get_attribute("placeholder"))
print(bug_link.text)
# driver.close()
driver.quit()
