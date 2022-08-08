# Generated by Django 4.0.6 on 2022-08-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totemApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='animalclass',
            name='classification',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='continents',
            name='continent',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='country',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='invertebrates',
            name='meaning',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='vertebrates',
            name='meaning',
            field=models.TextField(max_length=5000),
        ),
        migrations.AddField(
            model_name='invertebrates',
            name='keywords',
            field=models.ManyToManyField(to='totemApp.keywords'),
        ),
        migrations.AddField(
            model_name='vertebrates',
            name='keywords',
            field=models.ManyToManyField(to='totemApp.keywords'),
        ),
    ]