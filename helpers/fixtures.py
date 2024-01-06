import pytest
import random
from faker import Faker

fake = Faker()

@pytest.fixture
def random_string_generator():
    def random_string(length):
        return ''.join(fake.random_letters(length))
    return random_string

@pytest.fixture
def random_mail_generator():
    def random_mail():
        return fake.email()
    return random_mail

@pytest.fixture
def random_text_generator():
    def random_text():
        return fake.text()
    return random_text

@pytest.fixture
def random_state_generator():
    def random_state():
        return fake.state()
    return random_state

@pytest.fixture
def random_city_generator():
    def random_city():
        return fake.city()
    return random_city

@pytest.fixture
def random_postcode_generator():
    def random_postcode():
        return fake.postcode()
    return random_postcode

@pytest.fixture
def random_phone_generator():
    def random_phone():
        return fake.phone_number()
    return random_phone

@pytest.fixture
def random_address_generator():
    def random_address():
        return fake.address()
    return random_address

@pytest.fixture
def random_boolean_generator():
    def random_boolean():
        return random.choice([True, False])
    return random_boolean

@pytest.fixture
def increment():
    counter = [1]

    def increment_func():
        current_value = counter[0]
        counter[0] += 1
        return current_value

    yield increment_func

    counter[0] = 1