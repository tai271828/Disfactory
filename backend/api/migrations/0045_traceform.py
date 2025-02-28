# Generated by Django 2.2.13 on 2022-06-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_auto_20220607_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraceForm',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trace_type', models.IntegerField(blank=True, choices=[(0, '糞便'), (1, '腳印'), (2, '食痕'), (3, '折枝'), (4, '爪痕'), (5, '其他')], help_text='痕跡類型', null=True)),
                ('trace_type_desc', models.CharField(blank=True, help_text='痕跡類型描述', max_length=255, null=True)),
                ('age_type', models.IntegerField(choices=[(0, '新'), (1, '舊'), (2, '不清楚')], help_text='痕跡新舊類型')),
                ('age_days', models.IntegerField(blank=True, help_text='痕跡出現時間估計/日', null=True)),
                ('image_available', models.BooleanField(default=False, help_text='是否提供影像檔案')),
                ('other_info', models.CharField(blank=True, help_text='其他補充資訊', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
