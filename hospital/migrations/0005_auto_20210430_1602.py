# Generated by Django 3.1.5 on 2021-04-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20210430_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='price',
            field=models.FloatField(),
        ),
    ]
