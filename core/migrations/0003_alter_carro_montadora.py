# Generated by Django 4.1.2 on 2022-11-08 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_carro_motorista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='montadora',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.montadora'),
        ),
    ]
