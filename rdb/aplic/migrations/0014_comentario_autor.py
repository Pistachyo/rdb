# Generated by Django 4.2.6 on 2023-11-07 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0013_feedback_autor_feedback_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
