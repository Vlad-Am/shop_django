from django.db import models

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
    preview = models.ImageField(upload_to="catalog/", verbose_name="Изображение", **NULLABLE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", **NULLABLE)

    def __str__(self):
        return f"{self.name} цена: {self.price}, категория: {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("price",)

