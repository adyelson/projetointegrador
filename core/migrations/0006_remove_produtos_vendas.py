# Generated by Django 4.2 on 2023-05-27 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_produtos_vendas_alter_produtos_datacompra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='vendas',
        ),
    ]