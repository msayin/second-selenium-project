from behave import *
use_step_matcher('re')


@when ('I click on the link with id  "(".*)" ')

def step_imple(context, link_id):
    link = context.browser.find_element_by_id('blog-link')
    link.click()
