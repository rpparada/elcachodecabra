# Generated by Django 2.2.1 on 2020-05-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='promociones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='tamaño',
            field=models.CharField(blank=True, choices=[('FA', 'Familiar 38cm'), ('IN', 'Individual 20cm')], max_length=2),
        ),
    ]
