import datetime
from django.core.management.base import BaseCommand
from django.db.models import Sum

from ...exceptions import WeeklySalaryaClculationError
from ...models import DailyIncome, WeeklyIncome, Courier


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        today = datetime.date.today()
        idx = (today.weekday() + 1) % 7
        sat = today - datetime.timedelta(7 + idx - 6)

        qs = DailyIncome.objects.filter(
            insert_date__range=(datetime.date.today() - datetime.timedelta(7), datetime.date.today())).values(
            'courier').annotate(Sum('amount'))
        try:
            WeeklyIncome.objects.bulk_create(
                [WeeklyIncome(courier=Courier.objects.get(id=item['courier']), amount=item['amount__sum'], insert_date=sat)
                 for item in qs]
            )
            self.stdout.write(self.style.SUCCESS('Successfully calculate weekly income'))
        except:
            raise WeeklySalaryaClculationError
