# Generated by Django 4.0.2 on 2022-02-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_personal', '0003_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='estudiantes',
        ),
        migrations.AddField(
            model_name='group',
            name='estudiantes',
            field=models.ManyToManyField(to='control_personal.Student'),
        ),
    ]
