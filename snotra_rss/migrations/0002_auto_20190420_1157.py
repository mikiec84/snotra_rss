# Generated by Django 2.2 on 2019-04-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snotra_rss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterconfig',
            name='access_token_key',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='twitterconfig',
            name='access_token_secret',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='twitterconfig',
            name='consumer_key',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='twitterconfig',
            name='consumer_secret',
            field=models.CharField(max_length=100),
        ),
    ]
