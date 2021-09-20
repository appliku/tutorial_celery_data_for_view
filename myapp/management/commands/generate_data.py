from django.core.management.base import BaseCommand

from myapp.factories import PageViewFactory
from myapp.models import PageView


class Command(BaseCommand):
    def handle(self, *args, **options):
        PageView.objects.all().delete()
        PageViewFactory.create_batch(size=10000)

