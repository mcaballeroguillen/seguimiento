# Generated by Django 3.2.6 on 2021-09-17 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LineaBase', '0005_alter_temp_linea_base_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Encuestas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=15)),
                ('Encuesta', models.IntegerField()),
                ('Num_Pregunta', models.IntegerField()),
                ('Label', models.CharField(max_length=15)),
                ('Clase', models.CharField(max_length=50)),
                ('Frecuecia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=15)),
                ('Num_Encuesta', models.IntegerField()),
                ('Num', models.IntegerField()),
                ('Tipo', models.CharField(max_length=10)),
                ('Enunciado', models.CharField(max_length=100)),
                ('Opciones', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='temp_pregunta',
            name='Usuario',
            field=models.CharField(default=2, max_length=15),
            preserve_default=False,
        ),
    ]
