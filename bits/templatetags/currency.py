###############################################################################
## Imports
###############################################################################
from bits.currency import currency_format
from django import template


###############################################################################
## Filters
###############################################################################
register = template.Library()


@register.filter(name='currency2')
def currency2(dollars):
    try:
        dollars = float(dollars)
    except ValueError:
        return dollars

    # Convert to cents (integer)
    cents = int(dollars * 100)
    return currency_format(cents)


@register.filter(name='currency')
def currency(cents):
    return currency_format(cents)
