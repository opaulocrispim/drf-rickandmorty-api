# Generated by Django 4.0.4 on 2022-05-31 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rickandmorty', '0006_alter_personagem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodio',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='localizacao',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='genero',
            field=models.CharField(choices=[('D', 'Desconhecido'), ('M', 'Masculino'), ('F', 'Feminino')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='status',
            field=models.CharField(choices=[('D', 'Desconhecido'), ('M', 'Morto'), ('V', 'Vivo')], default='D', max_length=1),
        ),
    ]
