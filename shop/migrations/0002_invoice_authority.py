# Generated by Django 5.2.1 on 2025-06-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='authority',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
