# Generated by Django 3.0.4 on 2020-04-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamstudent', '0009_merge_20200402_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ausbildung_typ_medstud_famulaturen_allgemeinmedizin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentlistfiltermodel',
            name='ausbildung_typ_medstud_famulaturen_allgemeinmedizin',
            field=models.NullBooleanField(default=None),
        ),
    ]