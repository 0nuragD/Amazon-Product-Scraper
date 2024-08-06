from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Create data directory if it does not exist
if not os.path.exists("data"):
    os.makedirs("data")

driver = webdriver.Chrome()
query = "laptop"
file = 0
try:
    for i in range(1, 20):
        driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=38NAIC5XOXF0C&sprefix=laptop%2Caps%2C202&ref=nb_sb_noss_1")
        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        print(f"{len(elems)} items found")
        for elem in elems:
            d = elem.get_attribute("outerHTML")
            with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)
            file += 1

        time.sleep(2)
finally:
    driver.quit()
