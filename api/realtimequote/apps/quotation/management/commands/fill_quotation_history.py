from apps.quotation.tasks import collect_coin_quotation_history
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Executing command fill quotation history...")

        days = 30
        collect_coin_quotation_history.delay(days=days)

        print("Finished")
