# Generated by Django 5.0.6 on 2024-05-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faction',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
