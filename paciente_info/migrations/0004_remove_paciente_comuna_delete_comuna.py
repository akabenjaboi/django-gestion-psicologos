# Generated by Django 4.1.3 on 2022-11-21 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente_info', '0003_alter_paciente_comuna'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='comuna',
        ),
        migrations.DeleteModel(
            name='Comuna',
        ),
    ]
