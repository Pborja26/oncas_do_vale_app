# Generated by Django 4.2.17 on 2025-01-10 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='themeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_in', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_in', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_in', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=250)),
                ('theme_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.themetype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]