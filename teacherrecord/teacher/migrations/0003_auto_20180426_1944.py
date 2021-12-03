# Generated by Django 2.0.2 on 2018-04-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20180426_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='code',
            field=models.CharField(max_length=10, verbose_name='Assignment Code'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='field_of_interest',
            field=models.CharField(blank=True, max_length=100, verbose_name='Field of Interests'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='subjects',
            field=models.CharField(max_length=100, verbose_name='Subjects'),
        ),
    ]
