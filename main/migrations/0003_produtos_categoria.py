# Generated by Django 5.0.4 on 2024-05-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_produtos_nome_alter_produtos_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='categoria',
            field=models.CharField(choices=[('SMARTPHONE', 'SMARTPHONE'), ('VIDEOGAME', 'VIDEOGAME')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
