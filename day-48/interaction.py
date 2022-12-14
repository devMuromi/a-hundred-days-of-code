from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/Koi/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.set_window_size(1920, 1080)
driver.get("https://ja.wikipedia.org/wiki/")

# doc_count = driver.find_element(
#     By.CSS_SELECTOR, "#number > b:nth-child(1) > a:nth-child(1)"
# )

# print(doc_count.text)
# doc_count.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Muromi")
search_bar.send_keys(Keys.ENTER)

driver.quit()
