from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150,
                            unique="True",
                            verbose_name="Название")
    slug = models.SlugField(max_length=200,
                            blank="True",
                            null="True",
                            verbose_name="URL")

    # verbose_name для отображения названий полей класса

    def __str__(self):  # для отображения объектов этого класса
        return self.name

    class Meta:  # для отображения объектов этого класса
        # db_table = 'category' # имя для отображение в бд, не в admin
        verbose_name = 'Категорию товара'
        verbose_name_plural = 'Категории товара'


class Products(models.Model):
    name = models.CharField(max_length=150,
                            unique="True",
                            verbose_name="Название")
    slug = models.SlugField(max_length=200,
                            blank="True", null="True",
                            verbose_name="URL")
    description = models.TextField(blank="True", null="True",
                                   verbose_name="Описание")
    image = models.ImageField(upload_to='goods_images',
                              blank="True", null="True",
                              verbose_name="Изображение")
    price = models.DecimalField(default='0.00',
                                max_digits=7,
                                decimal_places=2,
                                verbose_name="Цена")
    discount = models.DecimalField(default='0.00',
                                   max_digits=4,
                                   decimal_places=2,
                                   verbose_name="Скидка в процентах")
    quantity = models.PositiveIntegerField(default=0,
                                           verbose_name="Кол-во")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE,
                                 verbose_name='Категория')

    class Meta:  # для отображения объектов этого класса
        # db_table = 'category' # имя для отображение в бд, не в admin
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):  # для отображения объектов этого класса
        return f'{self.name} Кол-во:{self.quantity} Цена:{self.price}'

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        return self.price
