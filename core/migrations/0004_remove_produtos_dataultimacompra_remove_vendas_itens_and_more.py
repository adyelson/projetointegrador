# Generated by Django 4.2 on 2023-05-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_descricao_produtos_nome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='dataUltimaCompra',
        ),
        migrations.RemoveField(
            model_name='vendas',
            name='itens',
        ),
        migrations.AddField(
            model_name='produtos',
            name='dataCompra',
            field=models.DateField(auto_now=True, verbose_name='Data Compra'),
        ),
        migrations.AddField(
            model_name='produtos',
            name='dataModificacao',
            field=models.DateField(auto_now=True, verbose_name='Data modificação'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='dataVenda',
            field=models.DateField(auto_now_add=True, verbose_name='Data Venda'),
        ),
        migrations.DeleteModel(
            name='ItemVendas',
        ),
    ]
