# Generated by Django 3.1.6 on 2021-06-23 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWEB', '0010_auto_20210623_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inkind',
            name='Count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inkind',
            name='Count1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inkind',
            name='Count2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inkind',
            name='Count3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monetary',
            name='Bills',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='settlement',
            name='Charges',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Fee',
            field=models.IntegerField(null=True),
        ),
    ]
