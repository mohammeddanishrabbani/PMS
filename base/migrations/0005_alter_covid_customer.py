# Generated by Django 3.2.9 on 2021-12-11 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_covid_no_of_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.customer'),
        ),
    ]