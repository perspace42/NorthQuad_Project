# Generated by Django 5.0.6 on 2024-05-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saga', '0006_unit_nummodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='cost',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unitType',
            field=models.CharField(choices=[('Hero', 'Hero'), ('Hearthguard', 'Hearthguard'), ('Warrior', 'Warrior'), ('Levy', 'Levy')], default='Hearthguard', max_length=20),
        ),
    ]
