from behave import *
from selenium import webdriver

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome()
    browser.get ('hppt://127.0.0.1:5000')

@then('I am on the blog page')
def step_impl(context):
    expected_url = 'hppt://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url

