# Generated by Django 4.2.4 on 2023-12-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_remove_pessoa_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
