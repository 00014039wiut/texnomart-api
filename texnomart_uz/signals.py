import json
import os

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from root.settings import BASE_DIR
from texnomart_uz.models import Product, Category


@receiver(post_save, sender=Product)
def product_save_email(sender, instance, created, **kwargs):
    if created:
        mail_subject = f"New Product {instance.name}"
        message = f"New Product {instance.name} is created"
        email_to = 'jasurmavlonov24@gmail.com'
        email_from = 'shohruxabdusaidov@gmail.com'
        send_mail(mail_subject, message, email_from, [email_to], fail_silently=False)


@receiver(post_save, sender=Category)
def category_save_email(sender, instance, created, **kwargs):
    if created:
        mail_subject = f"New Category {instance.name}"
        message = f"New Category {instance.name} is created"
        email_to = 'jasurmavlonov24@gmail.com'
        email_from = 'shohruxabdusaidov@gmail.com'
        send_mail(mail_subject, message, email_from, [email_to], fail_silently=False)


@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'deleted_products/', f'product_{instance.id}.json')

    product_data = {
        'id': instance.id,
        'name': instance.name,
        'price': instance.price,
        'description': instance.description,
        'category': instance.category.name
    }

    with open(file_path, mode='w') as file_json:
        json.dump(product_data, file_json, indent=4)

    print(f'{instance.name} is deleted')

@receiver(pre_delete, sender=Category)
def product_delete(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'deleted_categories/', f'category_{instance.id}.json')

    category_data = {
        'id': instance.id,
        'name': instance.name,
        'date': instance.date_added,
    }

    with open(file_path, mode='w') as file_json:
        json.dump(category_data, file_json, indent=4)

    print(f'{instance.name} is deleted')


@receiver(post_save, sender=User)
def save_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print(f"{instance.username} token saved")
