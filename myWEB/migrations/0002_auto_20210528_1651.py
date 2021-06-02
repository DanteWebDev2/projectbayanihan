# Generated by Django 3.1.6 on 2021-05-28 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myWEB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20, null=True)),
                ('Password', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Guest', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='option',
            old_name='viewer',
            new_name='sponsors',
        ),
        migrations.AddField(
            model_name='option',
            name='enters',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myWEB.enter'),
        ),
    ]
