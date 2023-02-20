from celery import Task
from realtimequote.celery import app
from realtimequote.coin_refresh_api_map import COIN_TO_BACKEND_API
from apps.coin.repository import CoinRepository
from utils import requests


@app.task(
    bind=True,
    queue="task-collect-coin-quotation",
    max_retries=5,
)
def collect_coin_quotation(self: Task) -> None:

    for (coin_name, backend) in COIN_TO_BACKEND_API.items():
        print(f"Collecting {coin_name}...")

        try:
            current_quote = backend.get_current_quote()
            CoinRepository.update_current_quote(current_quote)
        except requests.RequestExeption as e:
            print(e)
            self.retry(countdown=2)
        except Exception as e:
            raise e

        print(f"Completed collection of {coin_name}.")
