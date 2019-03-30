# Generated by Django 2.1.7 on 2019-03-30 07:27

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('gql', '0036_auto_20190330_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='logo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=0, size=[200, 200], upload_to='tag//', verbose_name='logo'),
        ),
    ]
