# Generated by Django 5.0.6 on 2024-05-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saga', '0005_alter_unit_sagadice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='equipment',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
