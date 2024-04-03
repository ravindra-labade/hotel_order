from django.db import models


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=20)
    hotel_address = models.CharField(max_length=20)
    table_no = models.IntegerField()
    no_of_persons = models.IntegerField()
    menu_list = models.CharField(max_length=20)
    total_bill = models.IntegerField()
    choice = [('Online', 'ONLINE'), ('Cash', 'CASH')]
    payment_mode = models.CharField(max_length=10, choices=choice)
