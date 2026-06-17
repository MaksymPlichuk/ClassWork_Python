from django.shortcuts import render
from django.utils.text import slugify

from categories.models import Category
from categories.forms import CategoryForm
from django.contrib import messages
from users.utils import save_custom_image

def category_list(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'categories/category_list.html', {'categories': categories} )

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                category = form.save(commit=False)
                if not category.slug:
                    category.slug = slugify(category.name, allow_unicode=False)
                if 'image' in request.FILES:
                    image = request.FILES['image']
                    image_name = save_custom_image(image, size=(600,600), folder='categories')
                    category.image=image_name
                category.save()
                messages.success(request, "Category successfully created")
                return redirect('categories:list')
            except Exception as e:
                messages.error(request, 'Category error', {str(e)})
        else:
            messages.error(request, "Corret errors in Form")
    else:
        form = CategoryForm()
    return render(request, 'categories/category_create.html', {'form':form} )    




