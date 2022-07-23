# Generated by Django 4.0.4 on 2022-05-31 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rickandmorty', '0004_alter_episodio_personagens_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personagem',
            old_name='id_personagem',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='personagem',
            name='status',
            field=models.CharField(choices=[('V', 'Vivo'), ('M', 'Morto'), ('D', 'Desconhecido')], default='D', max_length=1),
        ),
    ]
