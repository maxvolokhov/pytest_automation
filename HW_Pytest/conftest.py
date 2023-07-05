import pytest

from human import Human

import random


@pytest.fixture()
def create_human():
    human = Human(name='John', age=20, gender='male')
    yield human
    print('Human has been created!')

@pytest.fixture()
def create_human_male():
    human = Human(name='Stepan', age=30, gender='male')
    yield human
    print('Male has been created!')

@pytest.fixture()
def create_human_female():
    human = Human(name='Anna', age=27, gender='female')
    yield human
    print('Female has been created')

@pytest.fixture()
def random_gender_create():
    exist_gender = ['male', 'female']
    return random.choice(exist_gender)
