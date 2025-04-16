from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name='Категория товара')
    # verbose_name для отображения названий полей класса

    def __str__(self):  # для отображения объектов этого класса
        return self.title

    class Meta:            # для отображения объектов этого класса
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название продукта')
    price = models.FloatField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Кол-во')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name='Категория товара')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
