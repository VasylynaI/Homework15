import requests


class ApiRequests:
    def api_get_request(self, url: str):
        response = requests.get(url)
        print(response.json())
        return response

    def api_post_request(self, url: str, body: dict):
        response = requests.post(url=url, data=body)
        print(response.json())
        return response

    def api_get_post_parametrize(self, url: str, method: str, data=None):
        """

        Args:
            url: enter URL
            method: 'get','post'
            data: enter Data for POST method

        Returns:
            Request

        """
        if method == 'get':
            response = requests.get(url=url)
        elif method == 'post':
            response = requests.post(url=url, data=data)
        else:
            raise TypeError('Please use GET or POST method')
        return response
