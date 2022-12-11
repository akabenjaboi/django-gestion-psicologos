# Generated by Django 4.1.3 on 2022-11-17 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda_fecha', models.DateField()),
                ('psicologo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registar.psicologo')),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Agenda_hora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.agenda')),
                ('hora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.hora')),
            ],
        ),
    ]