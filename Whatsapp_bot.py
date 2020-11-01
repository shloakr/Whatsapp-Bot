#Python3
# this is works as of November 1, 2020
# Note there may be changes on the Whatsapp Web website causing this to not work. The elements could be removed.
from selenium import webdriver
import time
chrome_browser = webdriver.Chrome(
    executable_path='')  # location to the chrome driver
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(15)

user_name = 'user_name'  # user you want to send the message to

user = chrome_browser.find_element_by_xpath(
    '//span[@title="{}"]'.format(user_name))
user.click()

message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
# the message you want to send
message_box.send_keys('Hey, I am a whatsapp bot')

message_box = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
message_box.click()
