# Generated by Django 3.1.4 on 2020-12-10 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201210_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.CharField(max_length=32),
        ),
    ]
