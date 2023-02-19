from celery import Task
from realtimequote.celery import app
from realtimequote.coin_refresh_api_map import COIN_TO_BACKEND_API
from apps.coin.repository import CoinRepository
from apps.quotation.repository import QuotationRepository


@app.task(
    bind=True,
    queue="task-collect-coin-quotation-history",
    max_retries=20,
)
def collect_coin_quotation_history(self: Task, days: int) -> None:

    for (coin_name, backend) in COIN_TO_BACKEND_API.items():
        print(f"Collecting quotation history from {coin_name}...")
        coin = CoinRepository.get_coin_by_name(coin_name)
        quotation_history = backend.get_quote_history(days)
        
        QuotationRepository.bulk_create_quotation(quotation_history, coin)
        print(quotation_history)