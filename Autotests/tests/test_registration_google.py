import time
import uuid
import pytest


GOOGLE_LOGIN = (
    'fd4tr4555e@gmail.com'
)

GOOGLE_PASSWORD = (
    '123456qweRTY'
)


def test_registration_fb(user, url, selenium):
    selenium.implicitly_wait(15)
    selenium.get(url)
    registerClick = selenium.find_element_by_id('login-signup').click() # Search and click register button

    time.sleep(2) # Let the user actually see something!

    selenium.find_element_by_css_selector('#google-login > i').click() # Search and click facebook button
    time.sleep(2)
    window_before = selenium.window_handles[0]
    another_window = list(set(selenium.window_handles) - {selenium.current_window_handle})[0]
    selenium.switch_to.window(another_window) # Switch another window

    email = selenium.find_element_by_id('identifierId') # Input google email
    email.send_keys(GOOGLE_LOGIN)

    next = selenium.find_element_by_id('identifierNext')
    next.click()
    time.sleep(2)
    passwd = selenium.find_element_by_name('password') # Input google password
    passwd.send_keys(GOOGLE_PASSWORD)
    selenium.find_element_by_id('passwordNext').click()
    #passwordNext
    #time.sleep(1)

    selenium.switch_to_window(window_before) # Switch main window
    time.sleep(1)


    selenium.find_element_by_id('nav-bar--user-menu').click() # Search user menu and click
    selenium.find_element_by_id('user-menu--logout').click() # Search logout button menu and click

    print('Registration Google test success')
    selenium.quit()
