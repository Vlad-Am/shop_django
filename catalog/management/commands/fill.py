import json

from django.core.management import BaseCommand

from catalog.models import Products, Categories, Blog, Contacts


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """Здесь мы получаем данные из фикстуры с категориями"""
        with open("db_categories.json", "r", encoding="windows-1251") as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстуры с продуктами
        with open("db_products.json", "r", encoding="windows-1251") as file:
            return json.load(file)

    @staticmethod
    def json_read_contacts():
        # Здесь мы получаем данные из фикстуры с продуктами
        with open("db_contacts.json", "r", encoding="windows-1251") as file:
            return json.load(file)

    @staticmethod
    def json_read_blogs():
        # Здесь мы получаем данные из фикстуры с продуктами
        with open("db_blog.json", "r", encoding="windows-1251") as file:
            return json.load(file)

    def handle(self, *args, **options):

        # Удалите все продукты
        Products.objects.all().delete()
        # Удалите все категории
        Categories.objects.all().delete()
        # Удалите все контакты
        Contacts.objects.all().delete()
        # Удалите все записи блогов
        Blog.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []
        contacts_for_create = []
        blog_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Categories(pk=category["pk"], category=category["fields"]["category"],
                           description=category["fields"]["description"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Categories.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Products(name=product["fields"]["name"], description=product["fields"]["description"],
                         preview=product["fields"]["preview"],
                         # получаем категорию из базы данных для корректной связки объектов
                         category=Categories.objects.get(pk=product["fields"]["category"]),
                         price=product["fields"]["price"], created_at=product["fields"]["created_at"],
                         updated_at=product["fields"]["updated_at"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Products.objects.bulk_create(product_for_create)

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for contact in Command.json_read_contacts():
            contacts_for_create.append(
                Contacts(pk=contact["pk"], phone_number=contact["fields"]["phone_number"],
                         name=contact["fields"]["name"],
                         message=contact["fields"]["message"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Contacts.objects.bulk_create(contacts_for_create)

        for blog in Command.json_read_blogs():
            blog_for_create.append(
                Blog(title=blog["fields"]["title"],
                     content=blog["fields"]["content"],
                     slug=blog["fields"]["slug"],
                     preview=blog["fields"]["preview"],
                     created_at=blog["fields"]["created_at"],
                     published=blog["fields"]["published"],
                     view_count=blog["fields"]["view_count"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Blog.objects.bulk_create(blog_for_create)
