# Generated by Django 4.1.3 on 2022-12-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EshartApp', '0006_rename_city_travel_terminal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin1',
            name='site',
            field=models.CharField(max_length=30, null=True),
        ),
    ]