from django.core.management.base import BaseCommand
from blog.models import Category
from typing import Any

class Command(BaseCommand):
    help = "this command insets category data"
    def handle(self, *args: any, **options: any):
        #delete exiting data
        Category.objects.all().delete()
        Categories=['Sports','Technology','Science','Art','Food']
        for Category_name in Categories:
            Category.objects.create(name = Category_name)
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
