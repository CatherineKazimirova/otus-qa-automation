import requests
import pytest
from jsonschema import validate

base_url = 'https://jsonplaceholder.typicode.com/posts/'

post_body = {
    "title": "Lorem ipsum dolor sit amet",
    "body": "Lorem ipsum dolor sit amet",
    "userId": 1100
}


def test_posts_get():
    response = requests.get(base_url)
    assert response.status_code == 200, "Unexpected status code"
    for item in response.json():
        validate(item, {
            "type": "object",
            "properties": {
                "userId": {"type": "integer"},
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "body": {"type": "string"}
            },
        })


def test_posts_post():
    response = requests.post(base_url, json=post_body)
    assert response.status_code == 201, "Unexpected status code"
    validate(response.json(), {
        "type": "object",
        "properties": {
            "title": {"type": "string", "enum": ["Lorem ipsum dolor sit amet"]},
            "body": {"type": "string", "enum": ["Lorem ipsum dolor sit amet"]},
            "userId": {"type": "integer", "enum": [1100]},
            "id": {"type": "integer"},
        },
    })


def test_posts_put():
    response = requests.put(base_url + '5', json=post_body)
    assert response.status_code == 200, "Unexpected status code"
    validate(response.json(), {
        "title": "Lorem ipsum dolor sit amet",
        "body": "Lorem ipsum dolor sit amet",
        "userId": 1100,
        "id": 5
    })


@pytest.mark.parametrize('post_id', ['0', '123123123', 'one'])
def test_posts_not_found(post_id):
    response = requests.get(base_url + f'{post_id}')
    assert response.status_code == 404, "Unexpected status code"
    assert len(response.json()) == 0, "Quantity is not equal to expected"


@pytest.mark.parametrize('user_id', ['', '123123123', 'one'])
def test_posts_user_id_empty(user_id):
    response = requests.get(base_url + '?userId=' + f'{user_id}')
    assert response.status_code == 200, "Unexpected status code"
    assert len(response.json()) == 0, "Quantity is not equal to expected"


