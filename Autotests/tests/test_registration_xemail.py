import time
import uuid
import pytest


PASSWRD = (
    '123456qweRTY'
)

GOOGLE_PASSWORD = (
    '123456qweRTY'
)


def test_registration_fb(user, url, selenium):
    selenium.implicitly_wait(15)
    selenium.get(url)
    main_window = selenium.current_window_handle
    registerClick = selenium.find_element_by_id('login-signup').click() # Search and click register button

    Click = selenium.find_element_by_id('email-login').click() # Search and click vk button

    email = selenium.find_element_by_id('email') # Input email
    email.send_keys(user)

    selenium.find_element_by_css_selector('#app > div > div > div.loginSignup___24zvp > div > form > div.loginSignupLookup--formControl--action___2vWI7 > div').click() # Click next

    paswrd2 = selenium.find_element_by_id('password') # Input password
    paswrd2.send_keys(PASSWRD)

    paswrd2 = selenium.find_element_by_id('passwordConfirm') # Input password
    paswrd2.send_keys(PASSWRD)

    selenium.find_element_by_css_selector('#app > div > div > div.loginSignup___24zvp > div > form > div.signupForm--formControl--action___qCRSk > div').click() # Click pass
    check gmail mail
    body = selenium.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')
    selenium.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin', 'new_window')")
    selenium.switch_to_window(selenium.window_handles[1])
    time.sleep(10)
    selenium.find_element_by_css_selector('body > nav > div > a.gmail - nav__nav - link.gmail - nav__nav - link__sign - in').click() # Click pass
    selenium.get(selenium.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'))

    gmail = selenium.find_element_by_id('identifierId')  # Input email
    gmail.send_keys('fd4tr4555e@gmail.com')
    time.sleep(2)
    next = selenium.find_element_by_id('identifierNext')
    next.click()
    time.sleep(2)
    passwd = selenium.find_element_by_name('password')  # Input google password
    passwd.send_keys(GOOGLE_PASSWORD)
    selenium.find_element_by_id('passwordNext').click()
    time.sleep(20)
    selenium.find_element_by_id('nav-bar--user-menu').click() # Search user menu and click
    selenium.find_element_by_id('user-menu--logout').click() # Search logout button menu and click

    print('Registration email test success')
    selenium.quit()
