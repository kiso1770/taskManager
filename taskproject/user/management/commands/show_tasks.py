from django.core.management.base import BaseCommand, CommandError


class TasksList(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        print("Hello")