"""
Sends the `after_syncdb` signal.

"""

###############################################################################
## Imports
###############################################################################
from django.core.management.base import BaseCommand
from bits.general import after_syncdb


###############################################################################
## Command
###############################################################################
class Command(BaseCommand):
    help = 'sends after_syncdb signal'

    def handle(self, *args, **options):
        after_syncdb.send(sender=self)
        self.stdout.write('Sent after_syncdb\n')
