from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:

            self.slug = slugify(self.name)

            original_slug = self.slug
            queryset = Category.objects.filter(slug=self.slug)
            counter = 1

            while queryset.exists():
                self.slug = f"{original_slug}-{counter}"
                queryset = Category.objects.filter(slug=self.slug)
                counter += 1

        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_liked = models.BooleanField(default=False)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            queryset = Product.objects.filter(slug=self.slug)
            counter = 1
            while queryset.exists():
                self.slug = f"{original_slug}-{counter}"
                queryset = Product.objects.filter(slug=self.slug)
                counter += 1
        super(Product, self).save(*args, **kwargs)


class Key(models.Model):
    key_name = models.CharField(max_length=100)

    def __str__(self):
        return self.key_name


class Value(models.Model):
    value_name = models.CharField(max_length=100)

    def __str__(self):
        return self.value_name


class Attribute(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE, related_name='keys')
    value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name='values')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')

    class Meta:
        verbose_name_plural = 'Attributes'

    def __str__(self):
        return self.product.name


class Image(models.Model):
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.image_name
