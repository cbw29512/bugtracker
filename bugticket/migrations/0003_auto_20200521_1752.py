# Generated by Django 3.0.6 on 2020-05-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugticket', '0002_auto_20200521_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
