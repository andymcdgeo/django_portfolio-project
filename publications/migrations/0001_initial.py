# Generated by Django 2.2.12 on 2020-05-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_year', models.DateField()),
                ('pub_title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=500)),
                ('pub_body', models.CharField(max_length=200)),
                ('pub_type', models.CharField(max_length=200)),
                ('pub_doi', models.URLField()),
            ],
        ),
    ]