# Generated by Django 4.2 on 2023-05-27 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.CharField(max_length=200, verbose_name='Sequence')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
                ('precoCompra', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preço de Compra')),
                ('precoVenda', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preço de Venda')),
                ('grupo', models.CharField(max_length=100, verbose_name='Grupo')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca')),
                ('qtdEstoque', models.IntegerField(verbose_name='Quantidade em Estoque')),
                ('valorTotal', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor Total')),
                ('idGrade', models.IntegerField(verbose_name='Id Grade')),
                ('codFabrica', models.CharField(max_length=200, verbose_name='Código de Fábrica')),
                ('ncm', models.CharField(max_length=200, verbose_name='NCM')),
                ('situacaoFiscal', models.CharField(max_length=200, verbose_name='Situação Fiscal')),
                ('txRetorno', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Taxa de Retorno')),
                ('cest', models.CharField(max_length=200, verbose_name='CEST')),
                ('cstcsosn', models.CharField(max_length=200, verbose_name='CTS_CSOSN')),
                ('codBarras', models.CharField(max_length=200, verbose_name='Código de Barras')),
                ('localizacao', models.CharField(max_length=200, verbose_name='Localização')),
                ('valorCusto', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor de Custo')),
                ('dataUltimaCompra', models.DateField(verbose_name='Data Última Compra')),
            ],
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataUltimaVenda', models.DateField(verbose_name='Data Última Venda')),
                ('cpfcliente', models.CharField(max_length=200, verbose_name='CPF')),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
