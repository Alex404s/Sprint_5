from imports import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    return driver

@pytest.fixture
def driver_1():
    driver_1 = webdriver.Chrome()
    driver_1.maximize_window()
    driver_1.get("https://qa-desk.stand.praktikum-services.ru/")
    return driver_1

@pytest.fixture
def driver_2():
    driver_2 = webdriver.Chrome()
    driver_2.maximize_window()
    driver_2.get("https://qa-desk.stand.praktikum-services.ru/")
    return driver_2

@pytest.fixture
def driver_3():
    driver_3 = webdriver.Chrome()
    driver_3.maximize_window()
    driver_3.get("https://qa-desk.stand.praktikum-services.ru/")
    return driver_3

@pytest.fixture
def driver_4():
    driver_4 = webdriver.Chrome()
    driver_4.maximize_window()
    driver_4.get("https://qa-desk.stand.praktikum-services.ru/")
    return driver_4

@pytest.fixture
def driver_5():
    driver_5 = webdriver.Chrome()
    driver_5.maximize_window()
    driver_5.get("https://qa-desk.stand.praktikum-services.ru/")
    return driver_5

@pytest.fixture
def driver_6():
    driver_6 = webdriver.Chrome()
    driver_6.maximize_window()
    driver_6.get("https://qa-desk.stand.praktikum-services.ru/")
    return driver_6

@pytest .fixture
def random_email():
    random_email = f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 8)))}@{"ya.ru"}"
    return random_email

@pytest .fixture
def random_email_wrong():
    random_email_wrong = f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 8)))}"
    return random_email_wrong

@pytest .fixture
def pswd():
    pswd = 11111
    return pswd

@pytest .fixture
def pre_email():
    pre_email = "pre_user@ya.ru"
    return pre_email