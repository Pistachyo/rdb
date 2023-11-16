# Generated by Django 4.2.6 on 2023-10-31 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0006_evento_atracao_evento_equipamento_evento_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='atracao',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='equipamento',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='imagem',
        ),
        migrations.AddField(
            model_name='atracao',
            name='evento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.evento'),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='evento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.evento'),
        ),
        migrations.AddField(
            model_name='imagem',
            name='evento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.evento'),
        ),
    ]
