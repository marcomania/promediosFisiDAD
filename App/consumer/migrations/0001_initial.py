# Generated by Django 3.2.9 on 2021-12-02 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('codalu', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nomalu', models.CharField(max_length=50)),
                ('apealu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codcur', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nomcur', models.CharField(max_length=50)),
                ('credcur', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AluCur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notacur', models.IntegerField(default=4)),
                ('codalu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumer.alumno')),
                ('codcur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumer.curso')),
            ],
        ),
    ]
