# Generated by Django 2.2 on 2020-08-22 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200822_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='membership',
            field=models.CharField(blank=True, choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], default='Silver', max_length=100, null=True),
        ),
    ]