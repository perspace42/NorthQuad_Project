# Generated by Django 5.0.6 on 2024-05-25 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saga', '0006_alter_unit_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='aggMelee',
            field=models.FloatField(default=2),
        ),
        migrations.AlterField(
            model_name='unit',
            name='equipment',
            field=models.CharField(choices=[('Bows and Slings', 'Bows and Slings'), ('Composite Bows', 'Composite Bows'), ('Crossbows', 'Crossbows'), ('Heavy Weapons', 'Heavy Weapons'), ('Improvised Projectiles', 'Improvised Projectiles'), ('Javelins', 'Javelins'), ('Sarissa', 'Sarissa'), ('Unarmed', 'Unarmed'), ('Horse', 'Horse'), ('Horse, Cataphract', 'Horse, Cataphract'), ('Horse, Composite Bows', 'Horse, Composite Bows'), ('Horse, Javelin', 'Horse, Javelin'), ('Camel, Composite Bows', 'Camel, Composite Bows'), ('Camel, Javelin', 'Camel, Javelin'), ('-', '-')], default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='unit',
            name='specialRules',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unitName',
            field=models.CharField(default='Hearthguard', max_length=50),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unitType',
            field=models.CharField(choices=[('Warlord', 'Warlord'), ('Hearthguard', 'Hearthguard'), ('Warrior', 'Warrior'), ('Levy', 'Levy')], default='Hearthguard', max_length=20),
        ),
    ]
