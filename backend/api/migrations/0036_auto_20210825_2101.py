# Generated by Django 2.2.13 on 2021-08-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20210602_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='highlight_category',
            field=models.CharField(blank=True, choices=[('A', '新廠商寄居'), ('B', '倉儲'), ('C', '擴建')], max_length=1, null=True),
        ),
    ]
