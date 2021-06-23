# Generated by Django 3.1 on 2021-05-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=25, null=True)),
                ('phone_no', models.IntegerField()),
                ('date', models.DateField()),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('state', models.CharField(blank=True, max_length=25, null=True)),
                ('zip', models.IntegerField()),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]
