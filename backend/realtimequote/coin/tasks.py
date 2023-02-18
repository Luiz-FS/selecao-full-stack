from realtimequote.celery import app
from celery import Task


@app.task(
    bind=True,
    queue="task-collect-coin-quotation",
    max_retries=20,
)
def collect_coin_quotation(self: Task) -> None:
    print(f"Request {self.request!r}")
