from django.shortcuts import render, get_object_or_404
from .models import Products, PostImage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from math import ceil
from django.http import HttpResponse
#from django.views.generic import DetailView
# Create your views here.
def index(request):
    products=Products.objects.all()
    paginator=Paginator(products,6)
    page=request.GET.get('page')
    paged_products=paginator.get_page(page)

    context={
        'products':paged_products
    }
    return render(request,'index.html',context)


#def ProductDetailView(request, id): 
  #  product = get_object_or_404(Products, id=id)
  #  photos = PostImage.objects.filter(product=product)
  #  return render(request, 'details.html', {'product':product,'photos':photos })


def detail_view(request, id):
    product = get_object_or_404(Products, id=id)
    photos = PostImage.objects.filter(product=product)
    return render(request, 'details.html', {
        'product':product,
        'photos':photos
    })


