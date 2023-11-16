# Generated by Django 4.2.6 on 2023-10-17 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_doacao_delete_login'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'Comentário', 'verbose_name_plural': 'Comentários'},
        ),
        migrations.AlterModelOptions(
            name='doacao',
            options={'verbose_name': 'Doação', 'verbose_name_plural': 'Doações'},
        ),
        migrations.AlterModelOptions(
            name='endereco',
            options={'verbose_name': 'Endereço', 'verbose_name_plural': 'Endereços'},
        ),
        migrations.AlterModelOptions(
            name='equipamento',
            options={'verbose_name': 'Equipamento', 'verbose_name_plural': 'Equipamentos'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Feedback', 'verbose_name_plural': 'Feedbacks'},
        ),
        migrations.AlterModelOptions(
            name='parceria',
            options={'verbose_name': 'Parceria', 'verbose_name_plural': 'Parcerias'},
        ),
        migrations.RemoveField(
            model_name='pessoafisica',
            name='apelido',
        ),
    ]