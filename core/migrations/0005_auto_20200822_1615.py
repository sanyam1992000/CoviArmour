# Generated by Django 2.2 on 2020-08-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200822_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='Name', max_length=1000),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(default='Subject', max_length=1000),
        ),
    ]
