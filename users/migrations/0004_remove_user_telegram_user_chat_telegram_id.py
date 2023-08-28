# Generated by Django 4.2.4 on 2023-08-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_telegram_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telegram',
        ),
        migrations.AddField(
            model_name='user',
            name='chat_telegram_id',
            field=models.CharField(
                default=123,
                max_length=255,
                unique=True,
                verbose_name=' Ссылка на телеграмм'),
            preserve_default=False,
        ),
    ]
