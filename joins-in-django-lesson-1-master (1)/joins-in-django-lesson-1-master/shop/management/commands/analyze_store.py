from django.core.management.base import BaseCommand
from shop.models import *
from django.db.models import Max, Min, Avg, Count, Sum

class Command(BaseCommand):
    def handle(self, *args, **options):
        item_count = Item.objects.filter(category__name='Health Role').aggregate(total_items=Count('id'))
        print(item_count)

        price = Item.objects.aggregate(
            max_price=Max('price'),
            min_price=Min('price'),
            avg_price=Avg('price')
        )
        print(f"\nPrice for all items:\n Max: {price['max_price']}, Min: {price['min_price']}, Avg: {price['avg_price']}")

        categories = Category.objects.annotate(
            total_items=Count('items'),
            total_price=Sum('items__price', default=0)
        )

        for category in categories:
            print(f'Category: {category.name}, Total Items: {category.total_items}, Total Price: {category.total_price}')
        
        items_with_category = Item.objects.select_related('category').all()
        for item in items_with_category:
            print(f'Item: {item.name}, Category: {item.category.name}')

        items_with_tags = Item.objects.prefetch_related('tags').all()
        for item in items_with_tags:
            tag_names = [tag.name for tag in item.tags.all()]
            print(f'Item: {item.name}, Tags: {", ".join(tag_names) if tag_names else "No Tags"}')
