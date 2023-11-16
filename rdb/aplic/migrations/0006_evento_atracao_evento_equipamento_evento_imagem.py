# Generated by Django 4.2.6 on 2023-10-31 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_alter_comentario_options_alter_doacao_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='atracao',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.atracao'),
        ),
        migrations.AddField(
            model_name='evento',
            name='equipamento',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.equipamento'),
        ),
        migrations.AddField(
            model_name='evento',
            name='imagem',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.imagem'),
        ),
    ]
