# Generated by Django 3.2 on 2021-04-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0014_auto_20210420_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lalitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
