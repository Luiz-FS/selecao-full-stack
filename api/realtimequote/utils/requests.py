from http import HTTPStatus

import requests
from requests import ConnectionError, Timeout


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
