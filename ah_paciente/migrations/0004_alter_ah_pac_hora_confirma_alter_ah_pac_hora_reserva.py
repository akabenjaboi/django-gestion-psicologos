# Generated by Django 4.1.3 on 2022-12-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ah_paciente', '0003_ah_pac_confirmada_ah_pac_reservada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ah_pac',
            name='hora_confirma',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ah_pac',
            name='hora_reserva',
            field=models.DateTimeField(null=True),
        ),
    ]
