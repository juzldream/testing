#!/usr/bin/python
#-*- coding:utf-8 -*-
# date:17-11-05
# author:racher


from selenium import webdriver

print("start appform UI automation testing!")

# login appform
# definitiong variable

IP = "192.168.5.128" 
PORT = ":8080"
USERNAME = "jhadmin"
PASSWORD = "jhadmin"

driver = webdriver.Firefox()
driver.get("http://" + IP + PORT)

driver.find_element_by_id("j_username").send_keys(USERNAME)
driver.find_element_by_id("j_password").send_keys(PASSWORD)
driver.find_element_by_xpath("//input[@value='登   录']").click()


# testing 仿真计算





