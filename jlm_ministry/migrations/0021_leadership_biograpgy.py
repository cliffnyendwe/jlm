# Generated by Django 2.2 on 2020-04-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jlm_ministry', '0020_auto_20200421_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadership',
            name='biograpgy',
            field=models.CharField(default='biograpgy', max_length=1000),
        ),
    ]