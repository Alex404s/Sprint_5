import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import User_data

class TestLogout:
    def test_logout_success(self, driver):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        driver.find_element(*Locators.log_in).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.no_account))
        driver.find_element(*Locators.email_login).send_keys(User_data.pre_email)
        driver.find_element(*Locators.password_login).send_keys(User_data.pswd)
        driver.find_element(*Locators.enter).click()
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.nickname))
        driver.find_element(*Locators.exit).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        check_logout = driver.find_element(*Locators.log_in).text

        assert check_logout == "Вход и регистрация"      
        
        
