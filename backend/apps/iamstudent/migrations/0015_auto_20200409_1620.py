# Generated by Django 3.0.4 on 2020-04-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamstudent', '0014_emailtohospital_send_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailgroup',
            name='message',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='emailtohospital',
            name='message',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='emailtosend',
            name='message',
            field=models.TextField(default='', max_length=10000),
        ),
    ]
