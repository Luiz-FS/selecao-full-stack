from celery import Task
from realtimequote.celery import app
from backends.awesomeapi_quote_refresh_api import AwesomeapiQuoteRefresh
from apps.coin.repository import CoinRepository


COIN_TO_BACKEND_API = {
    "BRL / USD": AwesomeapiQuoteRefresh(name="BRL / USD", key="USD-BRL", data_key="USDBRL")
}


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
