from django.urls import path
from products import views

app_name='products'

urlpatterns=[
    path('', views.show_products, name="show_products"),
]