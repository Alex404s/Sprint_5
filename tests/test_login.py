from imports import *

class TestLogin:
    def test_login_success(self, driver_3, pswd, pre_email):

        WebDriverWait(driver_3, 3).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        driver_3.find_element(*Locators.log_in).click()

        WebDriverWait(driver_3, 3).until(expected_conditions.element_to_be_clickable(Locators.no_account))
        driver_3.find_element(*Locators.email_login).send_keys(pre_email)
        driver_3.find_element(*Locators.password_login).send_keys(pswd)
        driver_3.find_element(*Locators.enter).click()

        WebDriverWait(driver_3, 8).until(expected_conditions.visibility_of_element_located(Locators.nickname))
        WebDriverWait(driver_3, 8).until(expected_conditions.visibility_of_element_located(Locators.photo))
        check_user_info = driver_3.find_element(*Locators.user_info)
        
        assert check_user_info.get_attribute('class') == "header_flexRow__Xdqv1"
        
        driver_3.quit()




