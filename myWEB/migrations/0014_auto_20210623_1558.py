# Generated by Django 3.1.6 on 2021-06-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWEB', '0013_auto_20210623_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='Contact',
            field=models.IntegerField(null=True),
        ),
    ]
