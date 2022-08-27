import requests
import pytest
from jsonschema import validate

base_url = 'https://dog.ceo/'


def test_random_image_all_dogs():
    response = requests.get(base_url + 'api/breeds/image/random')
    assert response.status_code == 200, "Unexpected status code"
    validate(response.json(), {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string", "enum": ["success"]}
        },
    })


def test_count_random_image_all_dogs():
    response = requests.get(base_url + 'api/breeds/image/random/3')
    assert len(response.json()['message']) == 3, "Quantity is not equal to expected"


@pytest.mark.parametrize(('quantity', 'quantity_fact'), [(1, 1), (2, 2), (10, 10), (49, 49), (50, 50)])
def test_different_quantity_of_random_image_all_dogs(quantity, quantity_fact):
    response = requests.get(base_url + 'api/breeds/image/random/' + f'{quantity}')
    assert response.status_code == 200, "Unexpected status code"
    assert len(response.json()['message']) == quantity_fact, "Quantity is not equal to expected"


@pytest.mark.parametrize('quantity', [51, 1000])
def test_invalid_different_quantity_of_random_image_all_dogs(quantity):
    response = requests.get(base_url + 'api/breeds/image/random/' + f'{quantity}')
    assert response.status_code == 200, "Unexpected status code"
    assert len(response.json()['message']) == 50, "Quantity is not equal to expected"


def test_images_by_breed_not_found():
    response = requests.get(base_url + 'api/breed/qwert/images')
    assert response.status_code == 404, "Unexpected status code"
    response = requests.get(base_url + 'api/breed/qwert/images').json()
    validate(response, {
        "type": "object",
        "properties": {
            "status": {"type": "string", "enum": ["error"]},
            "message": {"type": "string", "enum": ["Breed not found (master breed does not exist)"]},
            "code": {"type": "integer", "enum": [404]}
        },
    },)

