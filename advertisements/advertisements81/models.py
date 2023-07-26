from django.db import models

# Create your models herуe
class Advertisements81(models.Model):
    title = models.CharField('заголовок', max_length = 128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text="Oтметьте, возможен ли торг")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    bu = models.BooleanField('б/у', help_text='Использовался ли товар', default=False)