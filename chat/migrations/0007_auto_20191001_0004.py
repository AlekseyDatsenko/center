# Generated by Django 2.2.5 on 2019-09-30 21:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20190923_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='author',
            new_name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Post', verbose_name='Новость'),
        ),
    ]