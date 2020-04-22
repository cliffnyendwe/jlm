# Generated by Django 2.2 on 2020-04-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jlm_ministry', '0008_pastors_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bishop',
            name='branch',
            field=models.CharField(choices=[('Main branch', 'Main branch'), ('Kitengela branch', 'Kitengela branch'), ('Kibera branch', 'Kibera branch')], default='branch', max_length=100),
        ),
        migrations.AlterField(
            model_name='pastors',
            name='branch',
            field=models.CharField(choices=[('Main branch', 'Main branch'), ('Kitengela branch', 'Kitengela branch'), ('Kibera branch', 'Kibera branch')], default='branch', max_length=100),
        ),
    ]