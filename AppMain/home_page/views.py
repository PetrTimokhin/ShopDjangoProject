from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
import random


def index(request):
    content = {
        'title': 'Home - Главная страница',
        'header': 'Магазин мебели HOME',
    }

    return render(request, 'home_page/index.html', content)


# @login_required(login_url='/users/register')
# @login_required

def about(request):
    content = {
        'title': 'Home - О нас',
        'header': 'О нас',
        'text_on_page': 'Текст о том какой классный этот интернет магазин.'
    }

    return render(request, 'home_page/about.html', content)


    # if request.user.is_authenticated:
    #     context = {'name': request.user.username, 'products': Product.objects.all()}
    # else:
    #     context = {'name': 'unknown', 'products': Product.objects.all()}

# заполнение БД товарами
    # # Названия для категорий и продуктов
    # category_titles = [
    #     "Электроника", "Одежда", "Игрушки", "Книги", "Косметика",
    #     "Мебель", "Продукты", "Бытовая техника", "Инструменты",
    #     "Аксессуары"
    # ]
    #
    # product_names = [
    #     "Ноутбук", "Футболка", "Медвежонок", "Роман", "Крем для лица",
    #     "Стул", "Хлеб", "Пылесос", "Отвертка", "Сумка"
    # ]
    #
    # # Очистим старые данные (по желанию)
    # Category.objects.all().delete()
    # Product.objects.all().delete()
    #
    # # Создаем категории
    # categories = []
    # for title in category_titles:
    #     cat = Category.objects.create(title=title)
    #     categories.append(cat)
    #
    # # Создаем продукты
    # for i in range(10):
    #     Product.objects.create(
    #         name=product_names[i],
    #         price=round(random.uniform(100, 10000), 2),
    #         quantity=random.randint(1, 100),
    #         category=random.choice(categories)
    #     )