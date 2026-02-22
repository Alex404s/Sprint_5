import random
import string

class Random_email:

    #Генерация случайного email адреса
    def random_email():
        random_email = f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 8)))}@{"ya.ru"}"
        return random_email

    #Генерация случайного email адреса не по маске  *******@*******.***
    def random_email_wrong():
        random_email_wrong = f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(1, 8)))}"
        return random_email_wrong