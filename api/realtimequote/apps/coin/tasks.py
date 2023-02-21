import logging

from apps.coin.repository import CoinRepository
from celery import Task
from utils import requests

from realtimequote.celery import app
from realtimequote.coin_refresh_api_map import COIN_TO_BACKEND_API

logger = logging.getLogger(__name__)


@app.task(
    bind=True,
    queue="task-collect-coin-quotation",
    max_retries=5,
)
def collect_coin_quotation(self: Task) -> None:
    for coin_name, backend in COIN_TO_BACKEND_API.items():
        logger.info(f"Collecting {coin_name}...")

        try:
            current_quote = backend.get_current_quote()
            CoinRepository.update_current_quote(current_quote)
        except requests.RequestExeption as e:
            logger.error(e)
            return self.retry(countdown=2)
        except Exception as e:
            raise e

        logger.info(f"Completed collection of {coin_name}.")
