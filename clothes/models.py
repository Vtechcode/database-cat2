from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    other_data = models.TextField(max_length=200)
    image = models.ImageField(upload_to='product_pics')
    product_category_name = models.CharField(max_length=50, default="none")
    category_name = models.CharField(max_length=50, null=True)
    colors = models.ManyToManyField('Colors', related_name='products', blank=True)
    size_code = models.CharField(max_length=50, null=True)  # Add this field for the size code

    def __str__(self):
        return self.product_name

class ApparelSize(models.Model):
    size_code = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sort_order = models.CharField(max_length=50)

class ProductCategories(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_category_name = models.CharField(max_length=50, default="none")
    def __str__(self):
        return self.product_category_name

class Categories(models.Model):
    parent_category_id = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Colors(models.Model):
    color_code = models.CharField(max_length=20)
    color_name = models.CharField(max_length=50)
    product = models.ManyToManyField(Product, related_name='product_colors')
    def __str__(self):
        return self.color_name