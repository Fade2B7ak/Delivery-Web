# Generated by Django 4.0.6 on 2022-07-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]