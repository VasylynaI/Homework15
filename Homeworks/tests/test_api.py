import json

from Homeworks.helper.api_requests import ApiRequests


class TestApiRequests:
    def setup_method(self):
        self.test_api = ApiRequests()

    def test_get_single_users(self):
        url = 'https://reqres.in/api/users/2'
        response = self.test_api.api_get_request(url)
        assert response.status_code == 200

    def test_post_user(self):
        url = 'https://reqres.in/api/users'
        body = {
            "name": "morpheus",
            "job": "leader"
        }
        response = self.test_api.api_post_request(url=url, body=body)
        assert json.loads(response.text).get('id')

    def test_parametrized_get_list_users(self):
        url = 'https://reqres.in/api/users?page=2'
        response = self.test_api.api_get_post_parametrize(url, 'get')
        assert response.status_code == 200

    def test_parametrized_post_user(self):
        url = 'https://reqres.in/api/users'
        create_data_user = {
            "name": "Joker",
            "job": "clown"
        }
        response = self.test_api.api_get_post_parametrize(url, 'post', create_data_user)
        assert response.status_code == 201
