# Generated by Django 4.2.2 on 2023-07-26 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('pais', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
