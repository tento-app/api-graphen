# Generated by Django 2.1.5 on 2019-02-01 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190131_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='大学')),
            ],
            options={
                'verbose_name': '大学',
                'verbose_name_plural': '大学',
            },
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '学部', 'verbose_name_plural': '学部'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'サークル', 'verbose_name_plural': 'サークル'},
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(blank=True, max_length=150, verbose_name='学部'),
        ),
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.ForeignKey(blank=True, help_text='Specific course for this user.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_set', related_query_name='user', to='users.Course', verbose_name='コース'),
        ),
    ]
