# Generated by Django 5.0.6 on 2025-02-16 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('nombre_lab', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('num_ordenadores', models.IntegerField()),
                ('email_tecnico', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('nombre_completo', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('laboratorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_inc.laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('numero_ordenador', models.CharField(max_length=10)),
                ('descripcion', models.TextField()),
                ('resuelta', models.BooleanField(default=False)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inc.laboratorio')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inc.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Resolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_resolucion', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('incidencia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion_inc.incidencia')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_inc.profesor')),
            ],
        ),
    ]
