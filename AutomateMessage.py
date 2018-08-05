from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://web.whatsapp.com/')

user = browser.find_element_by_class_name('_1wjpf').click()

msg_box = browser.find_element_by_class_name('_1Plpp')
msg_box.send_keys("Hello")
button = browser.find_element_by_class_name('weEq5').click()

