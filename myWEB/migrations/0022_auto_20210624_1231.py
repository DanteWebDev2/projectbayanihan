# Generated by Django 3.1.6 on 2021-06-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWEB', '0021_auto_20210624_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monetary',
            name='List',
        ),
        migrations.AddField(
            model_name='recipient',
            name='List',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
