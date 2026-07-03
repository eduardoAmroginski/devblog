from django.shortcuts import render, get_object_or_404
from .models import Artigo, Categoria

def home(request):

    categoria_selecionada = request.GET.get('categoria')

    categorias = Categoria.objects.all()
    
    if categoria_selecionada:
        noticias = Artigo.objects.filter(categoria__nome__icontains=categoria_selecionada)
    else:
        noticias = Artigo.objects.all()

    contexto = {
        'lista_artigos': noticias,
        'lista_categorias': categorias,
        'categoria_selecionada': categoria_selecionada
    }
    
    return render(request, "blog/index.html", contexto)


def sobre_nos(request):
    categorias = Categoria.objects.all()

    contexto = {
        'lista_categorias': categorias
    }

    return render(request, "blog/sobre.html", contexto)


def artigo_detalhe(request, id):
    categorias = Categoria.objects.all()

    noticia = get_object_or_404(Artigo, id=id)

    contexto = {
        'lista_categorias': categorias,
        'artigo': noticia
    }

    return render(request, 'blog/artigo_detalhe.html', contexto)