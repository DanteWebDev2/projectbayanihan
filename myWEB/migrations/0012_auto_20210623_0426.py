# Generated by Django 3.1.6 on 2021-06-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWEB', '0011_auto_20210623_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='Donors',
            field=models.CharField(choices=[('Monetary Donation', 'Monetary Donation'), ('In-Kind Donation', 'In-Kind Donation'), ('Both Donation', 'Both Donation')], max_length=20, null=True),
        ),
    ]
