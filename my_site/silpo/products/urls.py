from django.urls import path
from products import views

app_name='products'

urlpatterns=[
    path('', views.show_products, name="show_products"),
    path('create/', views.create_product, name="create"),
    path('<int:prod_id>/', views.show_one_product, name="one_product")
]