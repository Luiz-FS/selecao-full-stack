import requests
from requests import ConnectionError, Timeout
from http import HTTPStatus


class RequestExeption(Exception):
    ...


def get(url: str) -> dict:
    try:
        response = requests.get(url)

        if response.status_code != HTTPStatus.OK:
            raise RequestExeption()

        data = response.json()
        
        return data
    except (ConnectionError, Timeout) as e:
        raise RequestExeption(e)
    except Exception as e:
        raise e