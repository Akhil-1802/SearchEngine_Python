from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:word>', views.search, name='search'),
    path('text/<path:url>/',views.text,name='text')
]
