# Generated by Django 3.2.4 on 2021-06-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='name',
            field=models.CharField(default='init survey', max_length=250),
            preserve_default=False,
        ),
    ]