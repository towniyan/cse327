from django.urls import path, include

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.list, name = 'list'),
    path('create', views.create, name = 'create'),
    path('delete/<int:page_id>', views.delete, name = 'delete'),
]