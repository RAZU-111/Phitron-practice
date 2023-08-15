# Generated by Django 4.2.3 on 2023-08-14 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_studentinfomodel_teacherinfomodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('degination', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_app.employee')),
                ('take_interview', models.BooleanField()),
                ('hiring', models.BooleanField()),
            ],
            bases=('first_app.employee',),
        ),
    ]
