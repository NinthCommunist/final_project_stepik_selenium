import pytest
from selenium import webdriver

def test_guest_can_go_to_login_page(driver):
    login_link = driver.find_element_by_css_selector("#login_link")
    login_link.click()