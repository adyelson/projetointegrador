from django.db import models
from django.db.models import signals

class Produtos(models.Model):   
    nome = models.CharField('Nome', max_length=200)    
    precoVenda = models.DecimalField('Preço de Venda',decimal_places=2,max_digits=9)    
    qtdEstoque = models.IntegerField('Quantidade em Estoque')     
    dataModificacao = models.DateField('Data modificação', auto_now=True)
        
    def __str__ (self):
        return f'{self.nome}'
    
class Vendas(models.Model):
    dataVenda = models.DateTimeField('Data Venda', auto_now=True)    
    cpfCliente = models.CharField('CPF cliente', max_length=200)

    def __str__ (self):
        return f'{self.dataVenda} (CPF: {self.cpfCliente})'
  
class ItensVendas(models.Model):
    venda = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField('Quantidade')
    valorProdutoAplicado = models.DecimalField('Valor Aplicado Unidade',decimal_places=2,max_digits=9)
    valorTotal = models.DecimalField('Valor Total',decimal_places=2,max_digits=9)

    def __str__ (self):
        return f'{self.produto} ({self.quantidade})'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.produto.qtdEstoque -= self.quantidade
        self.produto.save()

    def delete(self, *args, **kwargs):
        self.produto.qtdEstoque += self.quantidade
        self.produto.save()
        super().delete(*args, **kwargs)
    
def atualizar_valor_produto_aplicado(sender, instance, **kwargs):
    instance.valorProdutoAplicado = instance.produto.precoVenda
    instance.valorTotal = instance.produto.precoVenda*instance.quantidade

# Registrar o sinal para o modelo ItensVendas antes de salvar
signals.pre_save.connect(atualizar_valor_produto_aplicado, sender=ItensVendas)