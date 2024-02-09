from django.core.management import BaseCommand


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Здесь мы получаем данные из фикстуры с категориями"""



    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):

        # Удалите все продукты
				# Удалите все категории

				# Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

				# Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(название_поля=значение_из_словаря, ..., название_поля=значение_из_словаря)
            )

				# Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

				# Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(название_поля=значение_из_словаря, ...,
												# получаем категорию из базы данных для корректной связки объектов
                        поле_категории=Category.objects.get(pk=значение_из_словаря), ...,
                        название_поля=значение_из_словаря)
            )

				# Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)