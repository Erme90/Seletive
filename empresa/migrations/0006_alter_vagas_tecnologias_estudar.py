# Generated by Django 4.1.3 on 2022-11-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_alter_vagas_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='tecnologias_estudar',
            field=models.ManyToManyField(null=True, related_name='estudar', to='empresa.tecnologias'),
        ),
    ]
