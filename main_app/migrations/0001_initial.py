# Generated by Django 2.2.6 on 2020-02-09 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('appoinment', models.CharField(max_length=30)),
                ('joining_date', models.DateField()),
            ],
        ),
    ]