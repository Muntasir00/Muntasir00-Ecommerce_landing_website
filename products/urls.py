from django.urls import path
from . import views
#from .views import ProductDetailView
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:id>/', views.detail_view, name='detail'),

]