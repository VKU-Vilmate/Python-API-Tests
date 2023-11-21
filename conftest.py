import pytest
import requests
from utilities.requestUtility import RequestUtility


@pytest.fixture()
def login():
    req = RequestUtility()
    creds = {
        "email": "vku_dev@vilmate.com",
        "password": "TestPassword"
    }
    token = req.post(endpoint='auth/login/', expected_status_code=200,
                     payload=creds)

    return token
