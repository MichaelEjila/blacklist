# Generated by Django 4.2.6 on 2023-10-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flaggeddata',
            name='data_value',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
