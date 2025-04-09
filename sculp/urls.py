from django.urls import path
from . import views
from .views import lista_tatuagens

urlpatterns = [
    path(
        '', views.index, name='index'
        ),
    path('shop/', views.shop, name='shop'),
    path("tatuagens/", lista_tatuagens, name="lista_tatuagens"),
]