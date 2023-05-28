from django.contrib import admin

from .models import Produtos, Vendas, ItensVendas

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):   
    list_display=('id','nome', 'precoVenda','qtdEstoque')
    
@admin.register(Vendas)
class VendasAdmin(admin.ModelAdmin):    
    list_display=('id','dataVenda','cpfCliente')

@admin.register(ItensVendas)
class ItensVendasAdmin(admin.ModelAdmin):    
    list_display=('id','venda','produto','quantidade')
    

# admin.site.register(Produtos, ProdutosAdmin)
# admin.site.register(Vendas, VendasAdmin)
# admin.site.register(ItensVendas, ItensVendasAdmin)

