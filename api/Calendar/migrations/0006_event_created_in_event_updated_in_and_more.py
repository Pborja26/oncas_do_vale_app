# Generated by Django 4.2.17 on 2025-01-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0005_eventtype_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_in',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='updated_in',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='eventpresence',
            name='created_in',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='eventpresence',
            name='updated_in',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='created_in',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='updated_in',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
