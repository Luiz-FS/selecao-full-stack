from backends.awesomeapi_quote_refresh_api import AwesomeapiQuoteRefresh
from backends.kraken_quote_refresh_api import KrakenQuoteRefresh

COIN_TO_BACKEND_API = {
    "BRL / USD": AwesomeapiQuoteRefresh(name="BRL / USD", key="USD-BRL", data_key="USDBRL"),
    "BTC / EUR": KrakenQuoteRefresh(
        name="BTC / EUR", key="XBTeur", data_key="XXBTZEUR", awesomeapi_coin_key="BTC-EUR"
    ),
    "BTC / USD": KrakenQuoteRefresh(
        name="BTC / USD", key="XBTusd", data_key="XXBTZUSD", awesomeapi_coin_key="BTC-USD"
    ),
}
