# Generated by Django 2.2.8 on 2020-01-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_modify_old_data_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factory',
            old_name='before_2016',
            new_name='before_release',
        ),
        migrations.AddField(
            model_name='factory',
            name='source',
            field=models.CharField(choices=[('G', '政府'), ('U', '使用者')], default='U', max_length=1),
        ),
    ]
