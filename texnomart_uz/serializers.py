from rest_framework import serializers

from texnomart_uz.models import Product, Category, Image, Attribute, Key, Value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    images = serializers.SerializerMethodField('get_images_url')
    attributes = serializers.SerializerMethodField('get_attributes')
    primary_image = serializers.SerializerMethodField('get_primary_image')

    def get_images_url(self, obj):
        request = self.context.get('request')
        images = obj.images.all()
        return [request.build_absolute_uri(image.image.url) for image in images]

    def get_attributes(self, obj):
        attributes = obj.attributes.all().values('key__key_name', 'value__value_name')
        product_attributes = {}
        for attribute in attributes:
            product_attributes[attribute['key__key_name']] = attribute['value__value_name']

        return product_attributes

    def get_primary_image(self, obj):
        images = obj.images.all()
        request = self.context.get('request')

        return request.build_absolute_uri(images[0].image.url)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = '__all__'


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'
