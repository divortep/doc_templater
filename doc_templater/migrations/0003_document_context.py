# Generated by Django 2.2 on 2019-04-21 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_templater', '0002_auto_20190420_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='context',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
