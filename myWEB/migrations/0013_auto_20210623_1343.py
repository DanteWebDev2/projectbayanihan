# Generated by Django 3.1.6 on 2021-06-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWEB', '0012_auto_20210623_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='Contact',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
