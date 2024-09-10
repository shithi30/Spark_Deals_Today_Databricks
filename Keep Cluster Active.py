# import
from selenium import webdriver
from selenium.webdriver.common.by import By

# open window
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# notebook
driver.get("https://community.cloud.databricks.com/?o=924599453726095#notebook/4004368016220956")

# login
driver.find_element(By.ID, "login-email").send_keys("shithi30@outlook.com")
driver.find_element(By.ID, "login-password").send_keys("Kaditchil123@\n")

# run
driver.find_element(By.XPATH, ".//button[@data-testid='notebook-run-all-button']").click()

# close window
driver.close()
