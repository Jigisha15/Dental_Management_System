# Generated by Django 4.1.6 on 2023-02-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('content', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]