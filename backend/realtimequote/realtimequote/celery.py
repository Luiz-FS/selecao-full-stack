from celery import Celery


app = Celery("realtimequote")
app.config_from_object("simple_settings:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.broker_transport_options = {
    "queue_order_strategy": "priority",
}