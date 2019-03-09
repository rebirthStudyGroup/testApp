# Generated by Django 2.1.7 on 2019-03-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail_address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=8)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
    ]
