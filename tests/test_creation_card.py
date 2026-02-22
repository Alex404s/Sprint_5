import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import User_data

class TestCreation:

    def test_creation_non_auth_failed(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.create_card))
        driver.find_element(*Locators.create_card).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.must_auth))
        check_must_auth = driver.find_element(*Locators.must_auth).text

        assert check_must_auth == "Чтобы разместить объявление, авторизуйтесь"


    def test_creation_auth_success(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        driver.find_element(*Locators.log_in).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.no_account))
        driver.find_element(*Locators.email_login).send_keys(User_data.pre_email)
        driver.find_element(*Locators.password_login).send_keys(User_data.pswd)
        driver.find_element(*Locators.enter).click()
        
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.nickname))
        driver.find_element(*Locators.create_card).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.card_name))
        driver.find_element(*Locators.card_name).send_keys('Плюшевые котики')
        driver.find_element(*Locators.card_description).send_keys('Мягкие, комфортные, прекрасные')
        driver.find_element(*Locators.card_cost).send_keys(777)
        driver.find_element(*Locators.card_dropdown_button_1).click()        
        driver.find_element(*Locators.card_dropdown_1).click()
        driver.find_element(*Locators.card_dropdown_button_2).click()
        driver.find_element(*Locators.card_dropdown_2).click()
        driver.find_element(*Locators.item_status_BU).click()
        driver.find_element(*Locators.public_button).click()

        WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(Locators.apply_button))
        driver.find_element(*Locators.photo).click()        

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.my_card_img))        
        creation = driver.find_element(*Locators.my_card_img)
        driver.execute_script("arguments[0].scrollIntoView();", creation) 
        check_img = driver.find_element(*Locators.my_card_img)

        assert check_img.get_attribute('alt') == 'Плюшевые котики'       
       