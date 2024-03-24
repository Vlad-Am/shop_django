from django.db import models
from pytils.translit import slugify

from users.models import User

# Create your models here.

NULLABLE = {"blank": True, "null": True}


class Categories(models.Model):
    category = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=100, verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return f"{self.category}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("category",)


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=100, verbose_name="Описание")
    preview = models.ImageField(upload_to="media/catalog", verbose_name="Изображение", **NULLABLE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец", **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return f"{self.name} цена: {self.price}, категория: {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("price",)

        permissions = [
            ("change_published", "отменять публикацию продукта",),
            ("change_description", "может менять описание любого продукта",),
            ("change_category", "может менять категорию любого продукта",)
        ]


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    phone_number = models.CharField(verbose_name="Телефон")
    message = models.TextField(verbose_name="Сообщение", **NULLABLE)

    def __str__(self):
        return f"Пользователь с именем: {self.name}\nТелефоном: {self.phone_number}\nПрислал сообщение: {self.message}"

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"
        ordering = ('name',)


class Blog(models.Model):

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, verbose_name="slug", **NULLABLE)
    content = models.TextField(verbose_name="Содержание", **NULLABLE)
    preview = models.ImageField(upload_to="catalog/blog", verbose_name="Изображение", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    published = models.BooleanField(verbose_name="Опубликовано", default=False)
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    price_per_one = models.FloatField(verbose_name="Цена за штуку", **NULLABLE)

    def __str__(self):
        return f"""Публикация с заголовком {self.title}\n создана {self.created_at}\n"""

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "публикации"
        ordering = ('price_per_one', 'created_at', 'view_count',)


class Version(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Продукт")
    number = models.FloatField(verbose_name="Номер версии")
    name = models.CharField(max_length=150, verbose_name="Название версии", **NULLABLE)
    working = models.BooleanField(verbose_name="Работает")

    def __str__(self):
        return f" Версия {self.product} номер {self.number}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ('product', 'number', 'name', 'working')
