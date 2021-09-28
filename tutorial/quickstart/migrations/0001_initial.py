# Generated by Django 3.2.7 on 2021-09-26 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(verbose_name='date of birth')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quickstart.author')),
            ],
        ),
    ]