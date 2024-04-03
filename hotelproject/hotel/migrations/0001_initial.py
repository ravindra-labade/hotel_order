# Generated by Django 5.0.3 on 2024-04-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=20)),
                ('hotel_address', models.CharField(max_length=20)),
                ('table_no', models.IntegerField()),
                ('no_of_persons', models.IntegerField()),
                ('menu_list', models.CharField(max_length=20)),
                ('total_bill', models.IntegerField()),
                ('payment_mode', models.CharField(choices=[('Online', 'ONLINE'), ('Cash', 'CASH')], max_length=10)),
            ],
        ),
    ]
