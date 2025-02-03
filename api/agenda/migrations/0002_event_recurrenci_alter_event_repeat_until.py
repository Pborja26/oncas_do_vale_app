# Generated by Django 4.2.18 on 2025-02-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='recurrenci',
            field=models.CharField(blank=True, choices=[('Unique', 'Unique'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='repeat_until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
