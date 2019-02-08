# Generated by Django 2.1.5 on 2019-02-03 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gql', '0013_auto_20190203_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[0-9a-z+]*$', '小英数字+だけね')], verbose_name='タグ'),
        ),
    ]
