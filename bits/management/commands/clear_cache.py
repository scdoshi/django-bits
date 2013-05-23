"""
Clears the cache via `django.core.cache.cache.clear`

::

    >>> python manage.py clear_cache
    Cleared Cache

"""
###############################################################################
## Imports
###############################################################################
from django.core.management.base import BaseCommand
from django.core.cache import cache


###############################################################################
## Command
###############################################################################
class Command(BaseCommand):
    help = 'clears django caches'

    def handle(self, *args, **kwargs):
        cache.clear()
        self.stdout.write('Cleared cache\n')
