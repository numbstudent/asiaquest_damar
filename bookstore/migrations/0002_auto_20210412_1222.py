# Generated by Django 3.1.6 on 2021-04-12 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='keywords',
        ),
        migrations.AddField(
            model_name='books',
            name='keywords',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Keywords',
        ),
    ]
