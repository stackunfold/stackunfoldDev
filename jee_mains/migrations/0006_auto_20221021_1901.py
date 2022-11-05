# Generated by Django 3.2.15 on 2022-10-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jee_mains', '0005_testseriesmap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jee_mains',
            name='options',
        ),
        migrations.AddField(
            model_name='jee_mains',
            name='option1',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='jee_mains',
            name='option2',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='jee_mains',
            name='option3',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='jee_mains',
            name='option4',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
