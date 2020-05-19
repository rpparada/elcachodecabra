# Generated by Django 2.2.1 on 2020-05-18 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('ingredientes', models.TextField(blank=True)),
                ('tamaño', models.CharField(blank=True, choices=[(0, 'Familiar'), (1, 'Individual')], max_length=2)),
            ],
        ),
    ]
