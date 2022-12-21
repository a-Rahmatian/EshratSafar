# Generated by Django 4.1.3 on 2022-11-09 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('kind', models.CharField(max_length=8)),
                ('reigstrationCode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('nationalCode', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=6)),
                ('birthDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='supporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('travelDate', models.DateField()),
                ('travelTime', models.TimeField()),
                ('travelKind', models.CharField(max_length=8)),
                ('capacity', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='EshartApp.company')),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='EshartApp.ticket')),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travel', to='EshartApp.travel')),
            ],
        ),
    ]