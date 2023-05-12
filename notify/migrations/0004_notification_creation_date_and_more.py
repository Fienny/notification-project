# Generated by Django 4.2 on 2023-05-03 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0003_alter_notification_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='category',
            field=models.CharField(choices=[('Танк', 'Танк'), ('Хил', 'Хил'), ('ДД', 'ДД'), ('Торговец', 'Торговец'), ('Гилдмастер', 'Гилдмастер'), ('Квестгивер', 'Квестгивер'), ('Кузнец', 'Кузнец'), ('Кожевник', 'Кожевник'), ('Зельевар', 'Зельевар'), ('Мастер Заклинаний', 'Мастер Заклинаний')], max_length=100),
        ),
    ]
