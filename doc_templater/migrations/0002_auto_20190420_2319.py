# Generated by Django 2.2 on 2019-04-20 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_templater', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='data',
            new_name='file_data',
        ),
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
