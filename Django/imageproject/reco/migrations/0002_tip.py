# Generated by Django 2.2.5 on 2019-10-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
