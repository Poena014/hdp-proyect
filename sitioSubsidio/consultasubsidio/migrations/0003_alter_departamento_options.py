# Generated by Django 3.2.3 on 2021-06-26 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultasubsidio', '0002_aplica_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['nombre']},
        ),
    ]
