from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView
from .models import Product
from django.http import Http404

# class Based View
class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

#Funcion Based View
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }    
    return render(request, 'products/list.html', context)

#class Based View
class ProductDetailView(DeleteView):
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return 
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance

#Funcion Based View
def product_detail_view(request, pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk=pk) 
    #instance = Product.objects.get_by_id(pk)
    qs = Product.objects.filter(id=pk)
    if qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404('Esse produto não exixte!')     
    
    context = {
        'object': instance
    }
    return render(request, 'products/detail.html', context)