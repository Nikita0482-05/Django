from django.core.management.base import BaseCommand

from blog.models import Blog


class Command(BaseCommand):
    help = "Отображение в консоли списка блогов"

    def handle(self, *args, **options):
        blogs = Blog.objects.all()
        if not blogs:
            print("Блоги отсутствуют")
            return

        for blog in blogs:
            print(f"ID: {blog.id}")
            print(f"Название: {blog.title}")
            print(f"Дата публикации: {blog.date_published}")
            print(f"Автор: {blog.author}", end="\n\n")
