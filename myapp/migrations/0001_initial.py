# Generated by Django 4.0.5 on 2022-07-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sID', models.CharField(max_length=10)),
                ('sName', models.CharField(max_length=30)),
                ('sPassword', models.CharField(max_length=30)),
                ('sEmail', models.EmailField(max_length=254)),
            ],
        ),
    ]