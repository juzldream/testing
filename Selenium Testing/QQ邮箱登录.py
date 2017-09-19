from selenium import webdriver
from time import sleep


# QQ mailbox login .

driver = webdriver.Firefox()

driver.get("https://mail.qq.com/")


driver.switch_to.frame("login_frame")
# driver.switch_to.frame(0)
# driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
sleep(4)

driver.find_element_by_xpath("//*[@id='switcher_plogin']").click()

driver.find_element_by_xpath('//*[@id="u"]').click()
driver.find_element_by_xpath('//*[@id="u"]').send_keys("1576768715@qq.com")

driver.find_element_by_xpath('//*[@id="p"]').click()
driver.find_element_by_xpath('//*[@id="p"]').send_keys("zr0702")

driver.find_element_by_xpath('//*[@id="login_button"]').click()

