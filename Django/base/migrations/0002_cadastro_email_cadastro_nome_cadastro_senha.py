# Generated by Django 4.2.10 on 2024-02-17 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='email',
            field=models.EmailField(default='default@email.com', max_length=50),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='nome',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='senha',
            field=models.CharField(default='12345', max_length=50),
        ),
    ]
