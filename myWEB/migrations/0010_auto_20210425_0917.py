# Generated by Django 3.1.6 on 2021-04-25 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWEB', '0009_auto_20210425_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='support',
            field=models.CharField(choices=[('button1', 'support'), ('button2', 'support')], default='none', max_length=10),
        ),
    ]
