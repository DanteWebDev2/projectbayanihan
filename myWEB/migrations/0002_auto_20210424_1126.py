# Generated by Django 3.1.6 on 2021-04-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWEB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Entry1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='Entry2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='Entry3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='Entry4',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='Entry5',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='Entry6',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
