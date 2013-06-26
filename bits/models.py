"""
Utility Model classes based on `models.Model`

"""

###############################################################################
## Imports
###############################################################################
# Python
from datetime import datetime

# Django
from django.conf import settings
from django.db import models
from django import get_version

DJANGO_VERSION = get_version()
if DJANGO_VERSION >= '1.4':
    from django.utils.timezone import now


###############################################################################
## Code
###############################################################################
def usetz_now():
    """Determine current time depending on USE_TZ setting.

    Affects Django 1.4 and above only. if `USE_TZ = True`, then returns
    current time according to timezone, else returns current UTC time.

    """
    USE_TZ = getattr(settings, 'USE_TZ', False)
    if USE_TZ and DJANGO_VERSION >= '1.4':
        return now()
    else:
        return datetime.utcnow()


###############################################################################
## Models
###############################################################################
class BaseModel(models.Model):
    """Abstract base class with auto-populated created and updated fields. """
    created = models.DateTimeField(default=usetz_now, db_index=True)
    updated = models.DateTimeField(default=usetz_now, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated = usetz_now()
        super(BaseModel, self).save(*args, **kwargs)
