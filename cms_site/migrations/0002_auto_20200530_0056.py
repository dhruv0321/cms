# Generated by Django 3.0.6 on 2020-05-29 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel('Films', 'Film'),
        migrations.RenameModel('Customers', 'Customer'),
        migrations.RenameModel('Seats', 'Seat'),
        migrations.RenameModel('Bookings', 'Booking'),
        migrations.RenameModel('Screenings', 'Screening'),
        migrations.RenameModel('Rooms', 'Room'),
    ]
