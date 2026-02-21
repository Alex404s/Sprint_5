from imports import *

class TestLogout:
    def test_logout_success(self, driver_4, pswd, pre_email):

        WebDriverWait(driver_4, 3).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        driver_4.find_element(*Locators.log_in).click()

        WebDriverWait(driver_4, 3).until(expected_conditions.element_to_be_clickable(Locators.no_account))
        driver_4.find_element(*Locators.email_login).send_keys(pre_email)
        driver_4.find_element(*Locators.password_login).send_keys(pswd)
        driver_4.find_element(*Locators.enter).click()
        
        WebDriverWait(driver_4, 5).until(expected_conditions.visibility_of_element_located(Locators.nickname))
        driver_4.find_element(*Locators.exit).click()

        WebDriverWait(driver_4, 5).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        check_logout = driver_4.find_element(*Locators.log_in).text

        assert check_logout == "Вход и регистрация"       
        
        driver_4.quit()
