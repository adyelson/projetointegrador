from django import forms
from .models import ItensVendas, Produtos, Vendas


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome','precoVenda','qtdEstoque']


class VendaModelForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['cpfCliente']

class ItensVendaModelForm(forms.ModelForm):
    class Meta:
        model = ItensVendas
        fields = ['produto','quantidade']

    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']
        produto = self.cleaned_data['produto']
        estoque = produto.qtdEstoque

        if quantidade > estoque:
            raise forms.ValidationError(f'Quantidade indisponível em estoque. (Disponível: {estoque})')

        return quantidade
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['produto'].queryset = Produtos.objects.filter(qtdEstoque__gt=0)