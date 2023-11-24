# Generated by Django 4.2.7 on 2023-11-24 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doacao',
            name='doador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pessoafisica',
            name='nome',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='pessoajuridica',
            name='nome',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
