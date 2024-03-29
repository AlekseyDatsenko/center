# Generated by Django 2.2.5 on 2019-09-22 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20190922_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('mail', models.EmailField(max_length=254, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'пользователя',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'обсуждение', 'verbose_name_plural': 'Форум'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.User', verbose_name='Пользователь')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.Post', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'Комметарии',
            },
        ),
    ]
