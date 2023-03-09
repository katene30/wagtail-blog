# Generated by Django 4.1.7 on 2023-03-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(help_text='Email Adress', max_length=100)),
                ('full_name', models.CharField(help_text='First and Last Name', max_length=100)),
            ],
        ),
    ]
