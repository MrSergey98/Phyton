# Generated by Django 4.2.11 on 2024-05-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_lawsuits_dates_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawsuits',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lawsuits_dates',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='responsible_for_lawsuits',
            name='info',
            field=models.TextField(null=True),
        ),
    ]
