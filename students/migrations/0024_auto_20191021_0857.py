# Generated by Django 2.2.3 on 2019-10-21 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0023_auto_20191015_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='father_cnic',
        ),
        migrations.RemoveField(
            model_name='student',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='fathers_phone_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='fathers_proffesion',
        ),
    ]