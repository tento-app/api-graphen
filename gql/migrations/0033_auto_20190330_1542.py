# Generated by Django 2.1.7 on 2019-03-30 06:42

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('gql', '0032_auto_20190329_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='logo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=0, size=[200, 200], upload_to='tag/', verbose_name='logo'),
        ),
    ]