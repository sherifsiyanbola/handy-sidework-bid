# Generated by Django 2.2 on 2020-01-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200101_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='i_will_be_available_in',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
