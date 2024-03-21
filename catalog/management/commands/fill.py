import json

from django.core.management import BaseCommand

from catalog.models import Products, Categories, Blog, Contacts, Version


class Command(BaseCommand):

    @staticmethod
    def json_read_db():
        with open("db/database.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def handle(self, *args, **options):
        # Тут, единственное, что не нашел как именно через пайчарм обнулить счетчик pk
        # Удаление всех продуктов
        Products.objects.all().delete()
        # # Удаление всех категорий
        Categories.objects.all().delete()
        # # Удаление всех контактов
        Contacts.objects.all().delete()
        # # Удаление всех записи блогов
        Blog.objects.all().delete()
        # # Удаление всех версии
        Version.objects.all().delete()

        # Создайте списки для хранения объектов.
        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте

        # Создаем объекты в базе с помощью метода bulk_create()
        Categories.objects.bulk_create(
            [
                Categories(pk=category['pk'], category=category["fields"]["category"],
                           description=category["fields"]["description"])

                for category in Command.json_read_db() if category['model'] == 'catalog.categories'
            ]
        )

        # Создаем объекты в базе с помощью метода bulk_create()
        Products.objects.bulk_create(
            [
                Products(pk= product['pk'], name=product["fields"]["name"],
                         description=product["fields"]["description"],
                         preview=product["fields"]["preview"],
                         category=Categories.objects.get(pk=product["fields"]["category"]),
                         price=product["fields"]["price"], created_at=product["fields"]["created_at"],
                         updated_at=product["fields"]["updated_at"])

                for product in Command.json_read_db() if product['model'] == 'catalog.products'
            ]
        )

        # Создаем объекты в базе с помощью метода bulk_create()
        Contacts.objects.bulk_create(
            [
                Contacts(phone_number=contact["fields"]["phone_number"],
                         name=contact["fields"]["name"],
                         message=contact["fields"]["message"])

                for contact in Command.json_read_db() if contact['model'] == 'catalog.contacts'
            ]
        )

        # Создаем объекты в базе с помощью метода bulk_create()
        Blog.objects.bulk_create(
            [
                Blog(title=blog["fields"]["title"],
                     content=blog["fields"]["content"],
                     slug=blog["fields"]["slug"],
                     preview=blog["fields"]["preview"],
                     created_at=blog["fields"]["created_at"],
                     published=blog["fields"]["published"],
                     view_count=blog["fields"]["view_count"]
                     )

                for blog in Command.json_read_db() if blog['model'] == 'catalog.blogs'
            ]
        )

        # Создаем объекты в базе с помощью метода bulk_create()
        Version.objects.bulk_create(
            [
                Version(product=Products.objects.get(pk=version["fields"]["product"]),
                        number=version["fields"]["number"], working=version["fields"]["working"])

                for version in Command.json_read_db() if version['model'] == 'catalog.version'
            ]
        )
