# Generated by Django 4.2.10 on 2024-02-26 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_cadastro_email_cadastro_nome_cadastro_senha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastro',
            options={'ordering': ['-data'], 'verbose_name': 'Formulário de contato', 'verbose_name_plural': 'Formulários de contatos'},
        ),
    ]