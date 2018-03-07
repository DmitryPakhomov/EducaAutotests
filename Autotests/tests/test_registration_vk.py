import time
import uuid
import pytest


VK_LOGIN = (
    '89627534861'
)

VK_PASSWORD = (
    '123456qweRTY'
)

VK_EMAIL = (
    'fkndjghd66@gmail.com'
)


def test_registration_fb(user, url, selenium):
    selenium.implicitly_wait(15)
    selenium.get(url)
    registerClick = selenium.find_element_by_id('login-signup').click() # Search and click register button

    time.sleep(2) # Let the user actually see something!

    vkClick = selenium.find_element_by_id('vk-login').click() # Search and click vk button
    time.sleep(2)
    #window_before = selenium.window_handles[0]
    #another_window = list(set(selenium.window_handles) - {selenium.current_window_handle})[0]
    #selenium.switch_to.window(another_window) # Switch another window

    phone = selenium.find_element_by_css_selector('#login_submit > div > div > input:nth-child(7)') # Input vk email
    phone.send_keys(VK_LOGIN)

    paswrd2 = selenium.find_element_by_css_selector('#login_submit > div > div > input:nth-child(9)') # Input vk password
    paswrd2.send_keys(VK_PASSWORD)

    selenium.find_element_by_id('install_allow').click() # Click login
    time.sleep(2)

    selenium.find_element_by_id('nav-bar--user-menu').click() # Search user menu and click
    selenium.find_element_by_id('user-menu--logout').click() # Search logout button menu and click

    print('Registration VK test success')
    selenium.quit()
