from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given('I open lkssau website')
def step_impl(context):
   context.browser.get("https://cabinet.ssau.ru/login")
@then('I print the title of website')
def step_impl(context):
   title = context.browser.title
   assert "Личный кабинет" in title

@given('I type wrong data')
def step_impl(context):
    context.browser.get("https://cabinet.ssau.ru/login")

@then('I see error message')
def step_impl(context):
    context.browser.find_element_by_name('name').send_keys("TestTest")
    context.browser.find_element_by_name('password').send_keys("123456")
    context.browser.find_element_by_class_name('passport-form__button').click()
    context.browser.implicitly_wait(250)
    danger_button = context.browser.find_element(By.XPATH, "//div[@class='my-2 text-danger text-center']/strong")
    print(danger_button.text)
    assert "Пользователя с таким логином и паролем не найдено" in danger_button.text

