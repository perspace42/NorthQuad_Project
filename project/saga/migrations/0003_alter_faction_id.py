# Generated by Django 5.0.6 on 2024-05-26 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saga', '0002_faction_id_alter_faction_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faction',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
