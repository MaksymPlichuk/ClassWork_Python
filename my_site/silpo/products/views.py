from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, ProductImage
from .forms import ProductForm
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.
def show_products(request):
    products = Product.objects.prefetch_related("images").all()
    return render(request, "products.html", {"products": products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                product = form.save(commit=False)
                if not product.slug:
                    product.slug = slugify(product.name, allow_unicode=False)
                product.save()
                images = request.FILES.getlist('images')
                for index, image in enumerate(images):
                    ProductImage.objects.create(
                        product=product,
                        image=image,
                        priority=index
                    )
                messages.success(request, 'Product created successfully')
                return redirect('products:show_products')

            except Exception as x:
                messages.error(request, f'Помилка створення продукту {str(x)}')
        else:
            messages.error(request, 'Виправте помилки у формі')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def show_one_product(request, prod_id):
    product = get_object_or_404(Product, id=prod_id)
    return render(request,"productPage.html", {"product":product})

