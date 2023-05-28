from django.urls import include, path
from .views import adicionar_itens, cadastrar_produto, delete_item, detalhar_venda, efetuar_venda, index, produto, produtodelete, produtos, vendadelete, vendas

urlpatterns = [
    path('', index, name='index'),
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
    path('efetuar_venda/', efetuar_venda, name='efetuar_venda'),
    path('detalhar_venda/<int:pk>', detalhar_venda, name='detalhar_venda'),
    path('adicionar_itens/<int:pk>', adicionar_itens, name='adicionar_itens'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('vendas/', vendas, name='vendas'),
    path('produtos/', produtos, name='produtos'),
    path('painel/core/produtos/<int:pk>/change', produto, name='produto'),
    path('painel/core/produtos/<int:pk>/delete', produtodelete, name='produtodelete'),
    path('painel/core/vendas/<int:pk>/delete', vendadelete, name='vendadelete'),
    path('accounts/', include('django.contrib.auth.urls')),   
]