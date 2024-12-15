from django.core.management.base import BaseCommand
from shop.models import Category, Item, Tag

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for category in Category.objects.with_item_count():
            print(f"Category: {category.name}, Item Count: {category.item_count}")

        
        for item in Item.objects.with_tag_count():
            print(f"Item: {item.name}, Tag Count: {item.tags_count}")

        
        for tag in Tag.objects.popular_tags(3):
            print(f"Tag: {tag.name}, Item Count: {tag.item_count}")
