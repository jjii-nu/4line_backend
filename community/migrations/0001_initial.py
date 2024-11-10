# Generated by Django 5.1.1 on 2024-11-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('trip_start', models.DateField()),
                ('trip_End', models.DateField()),
                ('region', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('content', models.TextField(max_length=500)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
