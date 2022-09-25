# Generated by Django 3.0.3 on 2020-07-24 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainname', models.CharField(max_length=30, null=True)),
                ('train_no', models.IntegerField(null=True)),
                ('from_city', models.CharField(max_length=30, null=True)),
                ('to_city', models.CharField(max_length=30, null=True)),
                ('departuretime', models.CharField(max_length=30, null=True)),
                ('arrivaltime', models.CharField(max_length=30, null=True)),
                ('trevaltime', models.CharField(max_length=100, null=True)),
                ('distance', models.IntegerField(null=True)),
                ('img', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Asehi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare', models.IntegerField(null=True)),
                ('train_name', models.CharField(max_length=30, null=True)),
                ('date3', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('add', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
       
        migrations.CreateModel(
            name='Add_route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=100, null=True)),
                ('distance', models.IntegerField(null=True)),
                ('fare', models.IntegerField(null=True)),
                ('train', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='railway.Add_Train')),
            ],
        ),
    ]
