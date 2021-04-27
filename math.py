from selenium import webdriver
import time 
web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfdXgTGBnIJG-RCDzV1nsCSITkTw3Wk06w8cDfl28mnoVbHnA/viewform');
time.sleep(1)
NAME = "Adithya Pai B"
BRANCH = "CS"
SECTION = "A"
Email = "paiadithya26@gmail.com"
email=web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
email.send_keys(Email)
USN = "4CB19CS002"
usn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
usn.send_keys(USN)
name = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(NAME)
branch = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
branch.send_keys(BRANCH)
section = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
section.send_keys(SECTION)
time.sleep(0.2)

printf("Done !\n")
printf("Dont forget to follow me on github @adithyapaib {^}_{^}")

