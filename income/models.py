from django.core.validators import MinValueValidator
from django.db import models


class Courier(models.Model):
    """
    Courier information
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)

    class Meta:
        db_table = 'Courier'


class Trip(models.Model):
    """
    Trip information
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    courier = models.ForeignKey(Courier, db_column='Courier', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Trip'


class Income(models.Model):
    """
    Income a trip
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    amount = models.BigIntegerField(db_column='Amount', validators=[MinValueValidator(0)])
    trip = models.OneToOneField(Trip, db_column='TripID', on_delete=models.CASCADE)
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
    insert_date = models.DateTimeField(db_column='InsertDate', auto_now_add=True)

    class Meta:
        db_table = 'IncreaseIncome'


class DeductionIncome(models.Model):
    """
    Deduction of income of couriers
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    amount = models.BigIntegerField(db_column='Amount')
    courier = models.ForeignKey(Courier, db_column='CourierID', on_delete=models.CASCADE)
    insert_date = models.DateTimeField(db_column='InsertDate', auto_now_add=True)

    class Meta:
        db_table = 'DeductionIncome'


class DailyIncome(models.Model):
    """
    store daily income
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    amount = models.BigIntegerField(db_column='Amount')
    courier = models.ForeignKey(Courier, db_column='CourierID', on_delete=models.CASCADE)
    insert_date = models.DateTimeField(db_column='InsertDate', auto_now_add=True)

    class Meta:
        db_table = 'DailyIncome'


class WeeklyIncome(models.Model):
    """
    Store weekly income
    """

    id = models.AutoField(db_column='ID', primary_key=True)
    amount = models.BigIntegerField(db_column='Amount')
    courier = models.ForeignKey(Courier, db_column='CourierID', on_delete=models.CASCADE)
    insert_date = models.DateTimeField(db_column='InsertDate', auto_now_add=True)  # first day of week

    class Meta:
        db_table = 'WeeklyIncome'

