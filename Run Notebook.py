# import
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# setup
from pyvirtualdisplay import Display
Display(visible = 0, size = (1920, 1080)).start()

# open window
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# notebook
driver.get("https://community.cloud.databricks.com/?o=924599453726095#notebook/879705943519200/command/4454688346219223")

# login
driver.find_element(By.ID, "login-email").send_keys("shithi30@outlook.com")
driver.find_element(By.ID, "login-password").send_keys(os.getenv("DATABRICKS_PASS") + "\n")

# run
driver.find_element(By.XPATH, ".//button[@data-testid='notebook-run-all-button']").click()

# close window
driver.close()
