# Generated by Django 3.2.9 on 2022-01-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_order_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='breathing_difficulty',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='cold',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='comorbid',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='covid',
            name='fever',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]