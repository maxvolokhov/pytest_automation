import pytest


def test_human_grow(create_human):
    human = create_human
    initial_age = human.age
    human.grow()
    assert human.age == initial_age + 1, 'Age should increase by 1 after calling grow()'


def test_age_not_negative(create_human):
    human = create_human
    human.grow()
    assert human.age >= 0, "Age should not be negative after calling grow()"


def test_human_change_gender(create_human_female):
    human = create_human_female
    initial_gender = human.gender
    human.change_gender('male')
    assert human.gender != 'female', 'Gender should be changed to female after calling change_gender()'
    assert human.gender != initial_gender, 'Gender should be different after calling change_gender()'


def test_age(create_human):
    human = create_human
    initial_age = human.age
    human.grow()
    assert human.age == initial_age + 1, "Human's Age should increase after calling grow()"


def test_validate_gender(create_human):
    human = create_human
    expected_gender = ['male', 'female']
    assert human.gender in expected_gender, 'Your gender is not recognisable'


@pytest.mark.parametrize('age', [98, 99, 100])
def test_alive_status(create_human, age):
    human = create_human
    age_limit = 100
    human.grow()
    assert age < age_limit, 'You are not alive'


def test_gender_random(create_human, random_gender_create):
    human = create_human
    human.change_gender(random_gender_create)
    assert human.gender == random_gender_create, 'Gender has been selected incorrectly'


def test_human_age(create_human, create_human_with_zeo_age):
    human = create_human
    assert 1 <= human.age <= 99, "Age should be set correctly"
    human2 = create_human_with_zeo_age
    assert human2.age == 0, "Age should be set to 0 by default"


def test_age_limit_reached(create_human):
    human = create_human
    age_limit = human._Human__age_limit
    for _ in range(age_limit):
        if human._Human__status == "alive":
            human.grow()
    assert human.age >= age_limit, "Age should reach or exceed the age limit"


def test_change_age(create_human):
    human = create_human
    initial_age = human.age
    changed_age = initial_age + 2
    assert changed_age - initial_age == 2, 'Age is not changed'
