# Generated by Django 4.2.2 on 2023-06-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_korisnik_last_login_korisnik_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='korisnik',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='password',
        ),
        migrations.AlterField(
            model_name='korisnik',
            name='email',
            field=models.CharField(max_length=64),
        ),
    ]
