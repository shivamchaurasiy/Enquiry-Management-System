# Generated by Django 4.2.4 on 2023-08-15 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_enquiry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('query', models.CharField(max_length=50)),
            ],
        ),
    ]