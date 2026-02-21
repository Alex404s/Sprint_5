from imports import *

class TestRegistration:

    def test_registration_new_user_success(self, driver, random_email, pswd):

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        driver.find_element(*Locators.log_in).click()    

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.no_account))
        driver.find_element(*Locators.no_account).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.email_create_acc))          
        driver.find_element(*Locators.email_create_acc).send_keys(random_email)
        driver.find_element(*Locators.password_create_acc).send_keys(pswd)
        driver.find_element(*Locators.submit_password_create_acc).send_keys(pswd)    
        driver.find_element(*Locators.create_acc_button).click()

        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.nickname))
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(Locators.photo))

        check_user_info = driver.find_element(*Locators.user_info)
        
        assert check_user_info.get_attribute('class') == "header_flexRow__Xdqv1"
        
        driver.quit()


    def test_registration_wrong_email_failed(self, driver_1, random_email_wrong):

        WebDriverWait(driver_1, 3).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        driver_1.find_element(*Locators.log_in).click()

        WebDriverWait(driver_1, 3).until(expected_conditions.element_to_be_clickable(Locators.no_account))
        driver_1.find_element(*Locators.no_account).click()       
        
        WebDriverWait(driver_1, 3).until(expected_conditions.element_to_be_clickable(Locators.email_create_acc))          
        driver_1.find_element(*Locators.email_create_acc).send_keys(random_email_wrong)
        driver_1.find_element(*Locators.create_acc_button).click()
        
        WebDriverWait(driver_1, 5).until(expected_conditions.visibility_of_element_located(Locators.email_field))
        driver_1.find_element(*Locators.email_error)
        driver_1.find_element(*Locators.password_error)
        driver_1.find_element(*Locators.submit_password_error)        
                
        check_error = driver_1.find_element(*Locators.error).text

        assert check_error == "Ошибка"

        driver_1.quit()


    def test_registration_exsisting_user_failed(self, driver_2, pswd, pre_email):
        WebDriverWait(driver_2, 3).until(expected_conditions.element_to_be_clickable((Locators.log_in)))
        driver_2.find_element(*Locators.log_in).click()

        WebDriverWait(driver_2, 3).until(expected_conditions.element_to_be_clickable((Locators.no_account)))
        driver_2.find_element(*Locators.no_account).click()

        WebDriverWait(driver_2, 3).until(expected_conditions.element_to_be_clickable((Locators.email_create_acc)))          
        driver_2.find_element(*Locators.email_create_acc).send_keys(pre_email)
        driver_2.find_element(*Locators.password_create_acc).send_keys(pswd)
        driver_2.find_element(*Locators.submit_password_create_acc).send_keys(pswd)
        driver_2.find_element(*Locators.create_acc_button).click()

        WebDriverWait(driver_2, 5).until(expected_conditions.visibility_of_element_located(Locators.email_field))
        driver_2.find_element(*Locators.email_error)
        driver_2.find_element(*Locators.password_error)
        driver_2.find_element(*Locators.submit_password_error) 

        check_error = driver_2.find_element(*Locators.error).text

        assert check_error == "Ошибка"

        driver_2.quit()
