# Generated by Django 2.0.5 on 2018-05-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KorisnikUOpasnosti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=25)),
                ('prezime', models.CharField(max_length=35)),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
    ]
