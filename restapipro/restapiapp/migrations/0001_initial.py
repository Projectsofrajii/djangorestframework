# Generated by Django 4.1.4 on 2023-01-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.BigIntegerField()),
                ('aadharno', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
