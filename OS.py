from selenium import webdriver
import time 
web = webdriver.Chrome()
web.get('file:///C:/Users/PC/Downloads/OPERATING%20SYSTEMS%20(4TH%20SEM%2018CS43).html');
time.sleep(1)
NAME = "Adithya Pai B"
BRANCH = "CS"
SECTION = "A"
USN="4CB19CS002"
Email = "paiadithya26@gmail.com"
email=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
email.send_keys(Email)
usn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
usn.send_keys(USN)
name = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(NAME)
section = web.find_element_by_xpath('//*[@id="i17"]/div[3]/div')
section.click()
section.click()
date = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
date.click()
date.click()