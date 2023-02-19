from celery import Task
from realtimequote.celery import app
from realtimequote.coin_refresh_api_map import COIN_TO_BACKEND_API
from apps.coin.repository import CoinRepository


@app.task(
    bind=True,
    queue="task-collect-coin-quotation",
    max_retries=20,
)
def collect_coin_quotation(self: Task) -> None:

    for (coin_name, backend) in COIN_TO_BACKEND_API.items():
        print(f"Collecting {coin_name}...")
        current_quote = backend.get_current_quote()
        CoinRepository.update_current_quote(current_quote)
        print(current_quote)
