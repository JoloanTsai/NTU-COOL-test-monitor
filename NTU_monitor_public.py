your_account = ""  # 輸入NTU COOL 帳號
your_password = ""  # 輸入NTU COOL 密碼
your_web_url = ""  # 輸入NTU COOL 線上測驗的網址
your_sound_path = ""  # 輸入播放提示音的音檔路徑

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = your_web_url
driver.get(url)

eles = driver.find_elements(By.CLASS_NAME, "LoginPage_w-80__7jxZJ")
print(eles)

NTUCC_LogIn = eles[1]


from selenium.webdriver.common.action_chains import ActionChains 

LogIn_1 = ActionChains(driver) 
LogIn_1.click(on_element = NTUCC_LogIn) 
LogIn_1.perform()  


account = driver.find_element(By.XPATH, "//input[@name='ctl00$ContentPlaceHolder1$UsernameTextBox']")
account.send_keys(your_account)
password = driver.find_element(By.XPATH, "//input[@name='ctl00$ContentPlaceHolder1$PasswordTextBox']")
password.send_keys(your_password)


LogIn_btn = driver.find_element(By.XPATH, "//input[@name='ctl00$ContentPlaceHolder1$SubmitButton']")

LogIn_2 = ActionChains(driver) 
LogIn_2.click(on_element = LogIn_btn) 
LogIn_2.perform()  


# 爬取測驗數量

import time

init_tests = driver.find_elements(By.CLASS_NAME, "ig-title")
init_tests_num = len(init_tests)

need_stop = False
while need_stop != True:
    tests = driver.find_elements(By.CLASS_NAME, "ig-title")
    print("現在總共有：" + str(len(tests)) + " 個測驗")

    if len(tests) != init_tests_num : break

    time.sleep(12)  # 重新整理延遲時間
    driver.refresh()
    time.sleep(1)


# 產生紀錄時間的文字檔
from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("現在的時間：", formatted_time)

file_name = "log_time.txt"
with open(file_name, "w") as file:
    file.write(formatted_time)



import pygame
pygame.init()

music_path = your_sound_path
pygame.mixer.music.load(music_path)

pygame.mixer.music.play()
pygame.time.Clock().tick(10)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# 關閉pygame
pygame.quit()

driver.close()


