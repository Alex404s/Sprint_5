from imports import *

class TestCreation:

    def test_creation_non_auth_failed(self, driver_5):
        WebDriverWait(driver_5, 3).until(expected_conditions.element_to_be_clickable(Locators.create_card))
        driver_5.find_element(*Locators.create_card).click()

        WebDriverWait(driver_5, 5).until(expected_conditions.visibility_of_element_located(Locators.must_auth))
        check_must_auth = driver_5.find_element(*Locators.must_auth).text

        assert check_must_auth == "Чтобы разместить объявление, авторизуйтесь"
        
        driver_5.quit()


    def test_creation_auth_success(self, driver_6, pswd, pre_email):
        WebDriverWait(driver_6, 3).until(expected_conditions.element_to_be_clickable(Locators.log_in))
        driver_6.find_element(*Locators.log_in).click()

        WebDriverWait(driver_6, 3).until(expected_conditions.element_to_be_clickable(Locators.no_account))
        driver_6.find_element(*Locators.email_login).send_keys(pre_email)
        driver_6.find_element(*Locators.password_login).send_keys(pswd)
        driver_6.find_element(*Locators.enter).click()
        
        WebDriverWait(driver_6, 8).until(expected_conditions.visibility_of_element_located(Locators.nickname))
        driver_6.find_element(*Locators.create_card).click()

        WebDriverWait(driver_6, 3).until(expected_conditions.element_to_be_clickable(Locators.card_name))
        driver_6.find_element(*Locators.card_name).send_keys('Плюшевые котики')
        driver_6.find_element(*Locators.card_description).send_keys('Мягкие, комфортные, прекрасные')
        driver_6.find_element(*Locators.card_cost).send_keys(777)
        driver_6.find_element(*Locators.card_dropdown_button_1).click()        
        driver_6.find_element(*Locators.card_dropdown_1).click()
        driver_6.find_element(*Locators.card_dropdown_button_2).click()
        driver_6.find_element(*Locators.card_dropdown_2).click()
        driver_6.find_element(*Locators.item_status_BU).click()
        driver_6.find_element(*Locators.public_button).click()

        WebDriverWait(driver_6, 8).until(expected_conditions.element_to_be_clickable(Locators.apply_button))
        driver_6.find_element(*Locators.photo).click()        

        WebDriverWait(driver_6, 5).until(expected_conditions.visibility_of_element_located(Locators.my_card_img))        
        creation = driver_6.find_element(*Locators.my_card_img)
        driver_6.execute_script("arguments[0].scrollIntoView();", creation) 
        check_img = driver_6.find_element(*Locators.my_card_img)

        assert check_img.get_attribute('alt') == 'Плюшевые котики'
        
        driver_6.quit()