# Generated by Django 3.1.4 on 2020-12-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201211_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='type',
            field=models.CharField(choices=[('R', 'race'), ('T', 'timerace'), ('P', 'physical'), ('K', 'knowledge')], default=('R', 'race'), max_length=1),
        ),
    ]
