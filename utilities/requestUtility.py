from data.hosts import DEV
import logging as logger
import requests
import json


class RequestUtility(object):

    def __init__(self):
        self.base_url = DEV

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
            f'Bad status code.' \
            f'Expected status code: {self.expected_status_code}, Actual status code: {self.status_code}' \
            f'URL: {self.url}, Response: {self.rs_json}'

    def get(self, endpoint, expected_status_code, payload=None, headers=None):
        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f'GET response: {rs_json}')

        return rs_json

    def post(self, endpoint, expected_status_code, payload=None, headers=None):
        self.url = self.base_url + endpoint

        rs_api = requests.post(url=self.url, json=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f'POST response: {self.rs_json}')

        return self.rs_json

    def patch(self, endpoint, expected_status_code, payload, headers):
        self.url = self.base_url + endpoint

        reg_api = requests.patch(url=self.url, json=payload, headers=headers)
        self.status_code = reg_api.status_code
        self.expected_status_code == expected_status_code
        self.rs_json = reg_api.json()
        self.assert_status_code()

        logger.debug(f'PATCH response: {self.rs_json}')

        return self.rs_json
