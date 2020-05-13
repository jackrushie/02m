from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')
chrome_browser.maximize_window()


assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

assert 'at-cv-lightbox-close' in chrome_browser.page_source
close_lightbox = chrome_browser.find_element_by_id('at-cv-lightbox-close')
close_lightbox.click()

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am Jack')

show_message_button.click()

chrome_browser.close()

# add waits into the programs.
# https://www.seleniumeasy.com/test/
