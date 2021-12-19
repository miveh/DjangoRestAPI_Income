import datetime
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from Income_calculation_partizaans.base_manager import BaseManager


class Courier(models.Model):
    """
    Courier information
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)

    class Meta:
        db_table = 'Courier'


class Income(models.Model):
    """
    Income a trip
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    amount = models.BigIntegerField(db_column='Amount', validators=[MinValueValidator(0)])
    courier = models.ForeignKey(Courier, db_column='CourierID', on_delete=models.CASCADE)
    insert_date = models.DateTimeField(db_column='InsertDate', auto_now_add=True)

    class Meta:
        db_table = 'Income'


class IncreaseIncome(models.Model):
    """
    Increase incomes of couriers
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    amount = models.BigIntegerField(db_column='Amount')
    courier = models.ForeignKey(Courier, db_column='CourierID', on_delete=models.CASCADE)
    insert_date = models.DateField(db_column='InsertDate', auto_now_add=True)

    class Meta:
        db_table = 'IncreaseIncome'


class DeductionIncome(models.Model):
    """
    Deduction of income of couriers
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    amount = models.BigIntegerField(db_column='Amount')
    courier = models.ForeignKey(Courier, db_column='CourierID', on_delete=models.CASCADE)
    insert_date = models.DateField(db_column='InsertDate', auto_now_add=True)

    class Meta:
        db_table = 'DeductionIncome'


class DailyIncome(models.Model):
    """
    store daily income
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    amount = models.BigIntegerField(db_column='Amount')
    courier = models.ForeignKey(Courier, db_column='CourierID', on_delete=models.CASCADE)
    insert_date = models.DateField(db_column='InsertDate', auto_now_add=True)

    objects = BaseManager()

    class Meta:
        db_table = 'DailyIncome'


class WeeklyIncome(models.Model):
    """
    Store weekly income
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    amount = models.BigIntegerField(db_column='Amount')
    courier = models.ForeignKey(Courier, db_column='CourierID', on_delete=models.CASCADE)
    insert_date = models.DateTimeField(db_column='InsertDate')  # first day of week

    class Meta:
        db_table = 'WeeklyIncome'


@receiver(post_save, sender=Income)
def update_income(sender, instance, created, **kwargs):
    if created:
        obj, create = DailyIncome.objects.get_or_create(insert_date=datetime.date.today(), courier=instance.courier, defaults={'amount': 0})
        obj.amount = F('amount') + instance.amount
        obj.save(update_fields=['amount'])


@receiver(post_save, sender=IncreaseIncome)
def update_increase(sender, instance, created, **kwargs):
    if created:
        obj = DailyIncome.objects.get_or_raise(courier=instance.courier, insert_date=datetime.date.today())
        obj.amount = F('amount') + instance.amount
        obj.save(update_fields=['amount'])


@receiver(post_save, sender=DeductionIncome)
def update_deduction(sender, instance, created, **kwargs):
    if created:
        obj = DailyIncome.objects.get_or_raise(insert_date=datetime.date.today(), courier=instance.courier)
        obj.amount = F('amount') - instance.amount
        obj.save(update_fields=['amount'])
