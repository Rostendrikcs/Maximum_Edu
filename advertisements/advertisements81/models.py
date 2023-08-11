from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
# Create your models herуe
User = get_user_model()

class Advertisements81(models.Model):
    title = models.CharField('заголовок', max_length = 128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text="Oтметьте, возможен ли торг")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    bu = models.BooleanField('б/у', help_text='Использовался ли товар', default=False)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='advertisements/')
    @admin.display(description='дата создания')
    def created_time_func(self):
        from django.utils import timezone
        if self.created_time.date() == timezone.now().date():
            created_time_2 = self.created_time.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time_2
            )
        return self.created_time.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='дата обновления')
    def updated_time_func(self):
        from django.utils import timezone
        if self.updated_time.date() == timezone.now().date():
            updated_time_2 = self.updated_time.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: orange; font-weight: bold;">Сегодня в {}</span>', updated_time_2
            )
        return self.updated_time.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f"Advertisements(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"