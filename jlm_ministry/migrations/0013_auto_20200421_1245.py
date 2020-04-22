# Generated by Django 2.2 on 2020-04-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jlm_ministry', '0012_chairman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairman',
            name='branch',
            field=models.CharField(choices=[('Main branch', 'Main branch'), ('Kitengela branch', 'Kitengela branch'), ('Kibera branch', 'Kibera branch'), ('Jlm ministries', 'Jlm ministries')], default='branch', max_length=100),
        ),
    ]