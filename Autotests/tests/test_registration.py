import time
import uuid
import pytest


SELECTOR_REGISTER_BTN = (
    'login-signup'   
)



def test_registration(user, url, selenium):
    selenium.implicitly_wait(15)
    selenium.get(url)

    registerClick = selenium.find_element_by_id(SELECTOR_REGISTER_BTN).click()

    time.sleep(2) # Let the user actually see something!

    fbClick = selenium.find_element_by_id('fb-login').click()

    googleClick = selenium.find_element_by_id('google-login').click()
    vkleClick = selenium.find_element_by_id('vk-login').click()



    pass1 = selenium.find_element_by_id('inputPassword')
    pass1.send_keys('******')

    pass2 = selenium.find_element_by_id('inputConfirmPassword')
    pass2.send_keys('******')

    team = selenium.find_element_by_id('inputCompany')
    team.send_keys('Test44')
    time.sleep(2) # Let the user actually see something!
    button = selenium.find_element_by_css_selector('body > div:nth-child(1) > div:nth-child(2) > div > div > div > div > div > form > button').click()

    selenium.find_element_by_id('nv-ava').click()
    selenium.find_element_by_id('nav-logout').click()

    print('Registration test success')
    selenium.quit()
