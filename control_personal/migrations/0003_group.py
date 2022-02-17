# Generated by Django 4.0.2 on 2022-02-17 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_personal', '0002_alter_address_city_alter_address_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiantes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_personal.student')),
                ('profesor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='control_personal.professor')),
            ],
        ),
    ]