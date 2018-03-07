import time
import uuid
import pytest


FACEBOOK_LOGIN = (
    'fotosymbol@gmail.com'
)

FACEBOOK_PASS = (
    '*******'
)


def test_registration_fb(user, url, selenium):
    selenium.implicitly_wait(15)
    selenium.get(url)
    registerClick = selenium.find_element_by_id('login-signup').click() # Search and click register button

    time.sleep(2) # Let the user actually see something!

    fbClick = selenium.find_element_by_id('fb-login').click() # Search and click facebook button
    time.sleep(2)
    window_before = selenium.window_handles[0]
    another_window = list(set(selenium.window_handles) - {selenium.current_window_handle})[0]
    selenium.switch_to.window(another_window) # Switch another window

    email = selenium.find_element_by_id('email') # Input facebook email
    email.send_keys(FACEBOOK_LOGIN)

    pas = selenium.find_element_by_id('pass') # Input facebook password
    pas.send_keys(FACEBOOK_PASS)

    selenium.find_element_by_id('u_0_0').click() # Click login
    selenium.switch_to_window(window_before) # Switch main window
    time.sleep(2)


    selenium.find_element_by_id('nav-bar--user-menu').click() # Search user menu and click
    selenium.find_element_by_id('user-menu--logout').click() # Search logout button menu and click

    print('Registration FB test success')
    selenium.quit()
