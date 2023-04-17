from django.db import models

class Produto(models.Model):
    sequence = models.CharField('Sequence', max_length=200)
    descricao = models.CharField('Descrição', max_length=200)
    tipo = models.CharField('Tipo', max_length=100)
    precoCompra = models.DecimalField('Preço de Compra',decimal_places=2,max_digits=9)
    precoVenda = models.DecimalField('Preço de Venda',decimal_places=2,max_digits=9)
    grupo = models.CharField('Grupo', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    qtdEstoque = models.IntegerField('Quantidade em Estoque')
    valorTotal = models.DecimalField('Valor Total',decimal_places=2,max_digits=9)
    idGrade = models.IntegerField('Id Grade')
    codFabrica = models.CharField('Código de Fábrica', max_length=200)
    ncm = models.CharField('NCM', max_length=200)
    situacaoFiscal = models.CharField('Situação Fiscal', max_length=200)
    txRetorno = models.DecimalField('Taxa de Retorno',decimal_places=2,max_digits=9)
    dataUltimaVenda = models.DateField('Data Última Venda')
    cest = models.CharField('CEST', max_length=200)
    cstcsosn = models.CharField('CTS_CSOSN', max_length=200)
    codBarras = models.CharField('Código de Barras', max_length=200)
    localizacao = models.CharField('Localização', max_length=200)
    valorCusto = models.DecimalField('Valor de Custo',decimal_places=2,max_digits=9)
    dataUltimaCompra = models.DateField('Data Última Compra')
    


    def __str__ (self):
        return f'{self.descricao} ({self.qtdEstoque})'
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__ (self):
        return self.email