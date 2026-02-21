import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from helpers import Random_email
from data import User_data


class TestRegistration:

    def test_registration_new_user_success(self, driver):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        driver.find_element(*Locators.log_in).click()    

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.no_account))
        driver.find_element(*Locators.no_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.email_create_acc))          
        driver.find_element(*Locators.email_create_acc).send_keys(Random_email.random_email())
        driver.find_element(*Locators.password_create_acc).send_keys(User_data.pswd)
        driver.find_element(*Locators.submit_password_create_acc).send_keys(User_data.pswd)    
        driver.find_element(*Locators.create_acc_button).click()

        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.nickname))
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.photo))

        check_user_info = driver.find_element(*Locators.user_info)
        
        assert check_user_info.get_attribute('class') == "header_flexRow__Xdqv1"        
      


    def test_registration_wrong_email_failed(self, driver):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        driver.find_element(*Locators.log_in).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.no_account))
        driver.find_element(*Locators.no_account).click()       
        
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.email_create_acc))          
        driver.find_element(*Locators.email_create_acc).send_keys(Random_email.random_email_wrong())
        driver.find_element(*Locators.create_acc_button).click()
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.email_field))
        driver.find_element(*Locators.email_error)
        driver.find_element(*Locators.password_error)
        driver.find_element(*Locators.submit_password_error)        
                
        check_error = driver.find_element(*Locators.error).text

        assert check_error == "Ошибка"

        


    def test_registration_exsisting_user_failed(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.log_in)))
        driver.find_element(*Locators.log_in).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.no_account)))
        driver.find_element(*Locators.no_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.email_create_acc)))          
        driver.find_element(*Locators.email_create_acc).send_keys(User_data.pre_email)
        driver.find_element(*Locators.password_create_acc).send_keys(User_data.pswd)
        driver.find_element(*Locators.submit_password_create_acc).send_keys(User_data.pswd)
        driver.find_element(*Locators.create_acc_button).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.email_field))
        driver.find_element(*Locators.email_error)
        driver.find_element(*Locators.password_error)
        driver.find_element(*Locators.submit_password_error) 

        check_error = driver.find_element(*Locators.error).text

        assert check_error == "Ошибка"       
