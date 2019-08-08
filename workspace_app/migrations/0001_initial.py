# Generated by Django 2.2.4 on 2019-08-07 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.CharField(max_length=15, unique=True)),
                ('topic', models.CharField(max_length=100)),
                ('pages', models.SmallIntegerField()),
                ('single_spaced', models.BooleanField(default=False, verbose_name='single spaced?')),
                ('slides', models.SmallIntegerField()),
                ('style', models.CharField(max_length=10)),
                ('date_due', models.DateTimeField()),
                ('task_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('task_cpp', models.FloatField()),
                ('task_academic_level', models.CharField(choices=[('HI', 'High School'), ('CO', 'College'), ('UN', 'University'), ('MA', 'Masters'), ('PH', 'PHD'), ('OT', 'Others')], max_length=2)),
                ('sources', models.SmallIntegerField()),
                ('task_type', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=20)),
                ('language', models.CharField(choices=[('ENGUK', 'English(U.K)'), ('ENGUS', 'English')], max_length=5)),
                ('task_status', models.CharField(choices=[('UA', 'Not Assigned'), ('AS', 'Assigned'), ('RE', 'On Revision'), ('CO', 'Completed'), ('CA', 'Cancelled'), ('OH', 'On hold'), ('TE', 'Test Task'), ('IQ', 'Inquiry')], max_length=2)),
                ('description', models.TextField()),
                ('comments', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.PositiveIntegerField()),
                ('alternate_telephone', models.PositiveIntegerField(blank=True)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('AC', 'Active'), ('SU', 'Suspended'), ('PR', 'Probation'), ('NA', 'Inactive')], default='AC', max_length=10)),
                ('academic_level', models.CharField(choices=[('HI', 'High School'), ('CO', 'College'), ('UN', 'University'), ('MA', 'Masters'), ('PH', 'PHD'), ('OT', 'Others')], default='UN', max_length=30)),
            ],
        ),
    ]
