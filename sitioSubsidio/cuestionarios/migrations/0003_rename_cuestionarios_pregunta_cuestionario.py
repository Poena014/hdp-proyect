# Generated by Django 3.2.3 on 2021-06-18 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionarios', '0002_alter_pregunta_cuestionarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregunta',
            old_name='cuestionarios',
            new_name='cuestionario',
        ),
    ]
