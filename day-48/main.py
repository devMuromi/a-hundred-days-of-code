from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Koi/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://python.org")

event_resources = driver.find_elements(
    By.CSS_SELECTOR, ".event-widget > div:nth-child(1) > ul.menu > li"
)
events = []

for event_resource in event_resources:
    events.append(
        {
            "time": event_resource.find_element(By.CSS_SELECTOR, "time").text,
            "name": event_resource.find_element(By.CSS_SELECTOR, "a").text,
            "url": event_resource.find_element(By.CSS_SELECTOR, "a").get_attribute(
                "href"
            ),
        }
    )

print(events)

driver.quit()
