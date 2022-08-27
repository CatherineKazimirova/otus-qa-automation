import requests
import pytest
from jsonschema import validate

base_url = 'https://api.openbrewerydb.org/'

brewery_response = {
    "type": "array",
    "items": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {"type": "string"},
        "address_3": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {"type": "string"},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "float"}
    },
}


def test_one_brewery_random():
    response = requests.get(base_url + 'breweries/random')
    assert response.status_code == 200, "Unexpected status code"
    validate(response.json(), brewery_response)


@pytest.mark.parametrize('query', ['인천맥주', '56', '10-56', 'BREWING', 'brewing', 'Brewing'])
def test_breweries_search_query(query):
    response = requests.get(base_url + 'breweries/search?query=' + f'{query}')
    assert response.status_code == 200, "Unexpected status code"
    assert len(response.json()) != 0


@pytest.mark.parametrize('by_type', ['', 'qwerty', '12345'])
def test_breweries_by_type_bad_request(by_type):
    response = requests.get(base_url + 'breweries?by_type=' + f'{by_type}')
    assert response.status_code == 400, "Unexpected status code"
    validate(response.json(), {
        "type": "object",
        "properties": {
            "errors": {"type": "array",
                       "items": {"type": "string",
                                 "enum": ["Brewery type must include one of these types: [\"micro\", \"nano\", "
                                          "\"regional\", \"brewpub\", \"large\", \"planning\", \"bar\", "
                                          "\"contract\", \"proprieter\", \"closed\"]"]}
                       },
        },
    })


@pytest.mark.parametrize(('pages', 'pages_fact'), [(1, 1), (2, 2), (25, 25), (49, 49), (50, 50)])
def test_breweries_per_page(pages, pages_fact):
    response = requests.get(base_url + 'breweries?per_page=' + f'{pages}')
    assert response.status_code == 200, "Unexpected status code"
    assert len(response.json()) == pages_fact, "Quantity is not equal to expected"


@pytest.mark.parametrize('dist', ['', '38.8977'])
def test_breweries_by_dist_bad_request(dist):
    response = requests.get(base_url + 'breweries?by_dist=' + f'{dist}')
    assert response.status_code == 400, "Unexpected status code"
    validate(response.json(), {
        "type": "object",
        "properties": {
            "errors": {"type": "array",
                       "items": {"type": "string",
                                 "enum": ["You must provide latitude and longitude for the 'by_dist' query param"]}
                       },
        },
    })


