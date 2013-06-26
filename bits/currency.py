"""
Currency related utilites.

"""
#
# External module elements
#
# 1. `currency` and `currency2`
#     template filters located in `bits.templatetags.currency`
#


###############################################################################
## Imports
###############################################################################
# Django
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models


# Extenal
if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^bits\.currency\.CurrencyField"])


###############################################################################
## Fields
###############################################################################
class CurrencyField(models.IntegerField):
    """Placeholder for CurrencyField. Add custom behaviour later. """
    pass


###############################################################################
## Formatting
###############################################################################
def currency_format(cents):
    """Format currency with symbol and decimal points.

    >> currency_format(-600)
    - $6.00

    TODO: Add localization support.
    """
    try:
        cents = int(cents)
    except ValueError:
        return cents

    negative = (cents < 0)
    if negative:
        cents = -1 * cents

    if cents < 100:
        dollars = 0
    else:
        dollars = cents / 100
        cents = cents % 100

    centstr = str(cents)
    if len(centstr) < 2:
        centstr = '0' + centstr

    if negative:
        return "- $%s.%s" % (intcomma(dollars), centstr)
    return "$%s.%s" % (intcomma(dollars), centstr)
