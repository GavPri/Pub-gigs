# Generated by Django 3.2.20 on 2023-07-25 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_guestlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='ticket_sales',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='GuestList',
        ),
    ]
