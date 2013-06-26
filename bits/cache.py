"""
Cache related utilites.

"""
#
# External module elements
#
# 1. `clear_cache`
#     management command in `bits.management.commands.clear_cache`
#

###############################################################################
## Constants
###############################################################################
HOUR_IN_SECONDS = 60 * 60
"""Constant for 1 hour in seconds (60 * 60)"""

DAY_IN_SECONDS = 24 * HOUR_IN_SECONDS
"""Constant for 1 day in seconds (24 * 60 * 60)"""

MONTH_IN_SECONDS = 30 * DAY_IN_SECONDS
"""Constant for 30 days in seconds (30 * 24 * 60 * 60)"""

YEAR_IN_SECONDS = 365 * DAY_IN_SECONDS
"""Constant for 1 year in seconds (365 * 24 * 60 * 60)"""
