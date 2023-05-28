from django.shortcuts import render, redirect
from .forms import  ProdutoModelForm, VendaModelForm, ItensVendaModelForm
from django.shortcuts import get_object_or_404
from .models import ItensVendas, Produtos, Vendas
from django.http import HttpResponse
from django.template import loader
from django.contrib import admin
from django.contrib import messages

# Create your views here.

def index(request):
    if str(request.user) != 'AnonymousUser':
        produtos = Produtos.objects.all()
        context = {
            'curso': 'Materiais de costura',
            'produtos': produtos,
        }
        return render(request,'index.html', context)
    else:
        return redirect('/accounts/login/')



def vendas(request):
    if str(request.user) != 'AnonymousUser':
        vendas = list(reversed(Vendas.objects.all()))
        contagem = len(vendas)
        for vendaAtual in vendas:            
            itens = ItensVendas.objects.filter(venda=vendaAtual.pk) 
            valorTotal = sum(item.valorTotal for item in itens)
            vendaAtual.total = valorTotal
        valorTotaldeTodas = sum(venda.total for venda in vendas)
        context = {
            'vendas' : vendas,
            'contagem':contagem,
            'valorTotaldeTodas':valorTotaldeTodas
        }
        return render(request,'vendas.html', context)
    else:
        return redirect('/accounts/login/')

def detalhar_venda(request, pk):
    if str(request.user) != 'AnonymousUser':  
        itens = list(reversed(ItensVendas.objects.filter(venda=pk))) 
        contagem = len(itens)
        valorTotal = sum(item.valorTotal for item in itens)
        context = {
            'itens' : itens,
            'valorTotal': valorTotal,
            'contagem':contagem
        }
        return render(request,'detalhar_venda.html', context)
    else:
        return redirect('/accounts/login/')

def efetuar_venda(request):
    if str(request.user) != 'AnonymousUser':
        vendaAtual = None
        if str(request.method)=='POST':
            formVenda = VendaModelForm(request.POST, request.FILES)
            
            if formVenda.is_valid():               
                vendaAtual = formVenda.save()
                
                
                formVenda = VendaModelForm()
                return redirect(f'/adicionar_itens/{vendaAtual.id}')
                # return redirect(f'/painel/core/vendas/{vendaAtual.id}/delete')
                
            else:
                messages.error(request, 'Erro ao iniciar venda.')
        else:            
            formVenda = VendaModelForm()
        context = {            
            'formVenda': formVenda,
            'vendaAtual': vendaAtual
        }
        return render(request,'efetuar_venda.html',context)
    else:
        return redirect('/accounts/login/')
    

def delete_item(request, item_id):
    item = get_object_or_404(ItensVendas, id=item_id)
    item.delete()
    return redirect(f'/adicionar_itens/{item.venda.id}')  # redireciona para a página desejada após a exclusão

def adicionar_itens(request, pk):
    if str(request.user) != 'AnonymousUser':
        vendaAtual = get_object_or_404(Vendas, id=pk)
        itens = list(reversed(ItensVendas.objects.filter(venda=pk)))
        valorTotal = sum(item.valorTotal for item in itens)
        contagem = len(itens)
        if str(request.method)=='POST':
            formItensVenda = ItensVendaModelForm(request.POST, request.FILES)            
            if formItensVenda.is_valid():  
                formItensVenda.instance.venda = vendaAtual             
                formItensVenda.save()
                return redirect(f'/adicionar_itens/{vendaAtual.id}')
                
            else:
                messages.error(request, 'Erro ao adicionar produto à venda.')
        else:
            formItensVenda = ItensVendaModelForm()

        context = {
            'formItensVenda': formItensVenda,
            'vendaAtual': vendaAtual,
            'itens': itens,
            'valorTotal': valorTotal,
            'contagem': contagem
        }
        return render(request,'adicionar_itens.html',context)
    else:
        return redirect('/accounts/login/')


def cadastrar_produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method)=='POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():               
                form.save()
                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request,'cadastrar_produto.html', context)
    else:
        return redirect('/accounts/login/')
    
def vendadelete(request, pk):
    if str(request.user) != 'AnonymousUser':
       return redirect('/painel/core/vendas/{% pk %}/delete')
    else:
        return redirect('/accounts/login/')


def produtodelete(request, pk):
    if str(request.user) != 'AnonymousUser':     
        return redirect('/painel/core/produtos/{% pk %}/delete')
    else:
        return redirect('/accounts/login/')

def produto(request, pk):
    if str(request.user) != 'AnonymousUser':
        # prod = Produto.objects.get(id=pk)
        # prod = get_object_or_404(Produtos, id=pk)
        # context = {
        #     'produto' : prod
        # }
        # return render(request,'produto.html', context)
        return redirect('/painel/core/produtos/{% pk %}/change')
    else:
        return redirect('/accounts/login/')
    

def produtos(request):
    if str(request.user) != 'AnonymousUser':
        produtos = Produtos.objects.all()
        context = {
            'produtos' : produtos
        }
        return render(request,'produtos.html', context)
    else:
        return redirect('/accounts/login/')



def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render, content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render, content_type='text/html; charset=utf8', status=500)