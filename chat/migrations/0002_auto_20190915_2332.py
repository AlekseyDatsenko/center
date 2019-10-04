# Generated by Django 2.2.5 on 2019-09-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.TextField()),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Обсуждения', 'verbose_name_plural': 'Обсуждение'},
        ),
    ]
