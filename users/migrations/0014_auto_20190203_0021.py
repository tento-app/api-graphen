# Generated by Django 2.1.5 on 2019-02-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gql', '0006_auto_20190203_0021'),
        ('users', '0013_auto_20190202_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Specific tags for this user.', related_name='teams', to='gql.Tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='user',
            name='content',
            field=models.TextField(blank=True, verbose_name='User content'),
        ),
        migrations.AddField(
            model_name='user',
            name='header',
            field=models.URLField(blank=True, verbose_name='header'),
        ),
        migrations.AddField(
            model_name='user',
            name='logo',
            field=models.URLField(blank=True, verbose_name='logo'),
        ),
        migrations.AddField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Specific tags for this user.', related_name='users', to='gql.Tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(blank=True, verbose_name='url'),
        ),
    ]
