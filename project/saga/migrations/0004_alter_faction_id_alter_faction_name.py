# Generated by Django 5.0.6 on 2024-05-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saga', '0003_alter_faction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faction',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='faction',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
