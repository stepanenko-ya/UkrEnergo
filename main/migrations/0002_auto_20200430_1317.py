# Generated by Django 3.0.5 on 2020-04-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
