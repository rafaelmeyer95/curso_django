# Generated by Django 3.2.7 on 2021-09-12 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210911_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('publicado',)},
        ),
    ]
