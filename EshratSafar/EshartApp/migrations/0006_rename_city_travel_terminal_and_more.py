# Generated by Django 4.1.3 on 2022-12-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EshartApp', '0005_rename_phonenumber_supporter_phonenumber2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel',
            old_name='city',
            new_name='terminal',
        ),
        migrations.AlterField(
            model_name='supporter',
            name='phoneNumber1',
            field=models.CharField(default='0', max_length=11),
        ),
    ]