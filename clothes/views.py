from django.shortcuts import render, HttpResponse
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, ApparelSize, ProductCategories, Categories, Colors

# Create your views here.

def home(request):
    clad = Product.objects.all()

    return render(request, 'clothes\home.html', {'clads':clad})

class ClothesList(ListView):
    model = Product
    template_name = 'clothes/home.html'
    context_object_name = 'clads'

class ClothesDetails(DetailView):
    model = Product
    template_name = 'clothes/clothes_detail.html'
    context_object_name = 'clad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        # Add information from extended models to the context
        context['apparel_sizes'] = product.apparelsize_set.all()
        context['product_categories'] = product.productcategories_set.all()
        context['categories'] = Categories.objects.filter(parent_category_id__in=context['product_categories'])
        context['colors'] = product.colors.all()

        return context

class ClothesCreate(CreateView):
    model = Product
    success_url = reverse_lazy('clad')
    fields = '__all__'
    template_name = 'clothes/clothes_create.html'

    def form_valid(self, form):
        # Save the Product instance
        product = form.save()

        # Get related data from the form
        product_category_name = form.cleaned_data.get('product_category_name')
        category_name = form.cleaned_data.get('category_name')
        color_names = form.cleaned_data.get('colors')
        size_code = form.cleaned_data.get('size_code')

        # Create ProductCategories instance and link it to the new product.
        if product_category_name:
            product_category = ProductCategories.objects.create(product=product, product_category_name=product_category_name)
        
            # Create Categories instance and link it to the new product category.
            if category_name:
                Categories.objects.create(parent_category_id=product_category, category_name=category_name)

        # Link Colors instances to the new product.
        if color_names:
            product.colors.set(color_names)

        # Create ApparelSize instance and link it to the new product.
        if size_code:
            apparel_size = ApparelSize.objects.create(size_code=size_code, product=product)

        return super().form_valid(form)

class ClothesUpdate(UpdateView):
    model = Product
    success_url = reverse_lazy('clad')
    template_name = 'clothes/clothes_create.html'
    fields = '__all__'


class ClothesDelete(DeleteView):
    model = Product
    template_name = 'clothes/clothes_delete.html'
    context_object_name = 'clad'
    success_url = reverse_lazy('clad')