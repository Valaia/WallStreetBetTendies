"""tendies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import get_stock_tick_data, delete_stock_tick_data, insert_stock_tick_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'tick_data/<str:stock_symbol>/<str:start_date>/<str:end_date>', 
        get_stock_tick_data, 
        name='get_stock_tick_data'
    ),
    path(
        'delete_tick_data/<str:stock_symbol>',
        delete_stock_tick_data,
        name='delete_stock_tick_data'
    ),
    path(
        'insert_tick_data/<str:stock_symbol>',
        insert_stock_tick_data,
        name='insert_stock_tick_data'
    )
]
