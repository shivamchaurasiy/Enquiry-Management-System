# Generated by Django 4.1.6 on 2023-08-13 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_enquiry', '0002_adminsingup_delete_admindatabase'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminSingUp',
            new_name='AdminSignUp',
        ),
    ]