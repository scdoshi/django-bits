*******
general
*******

.. automodule:: bits.general


functions
=========

.. autofunction:: bits.general.get_or_none

.. autofunction:: bits.general.get_profile_model


commands
========

:mod:`after_syncdb`
-------------------

.. automodule:: bits.management.commands.after_syncdb
    :members:
    :undoc-members:


This can be useful in a deploy script scenario where you want to run certain django operations after syncdb or migrate have completed. ``post_syncdb`` and ``post_migrate`` get triggered after every app and it's difficult to check if a few apps have been synced already. In such cases you can just set your app run certain operations on recieving ``after_syncdb`` and then do thid in your deploy script:


::

    $ python manage.py syncdb
    $ python manage.py after_syncdb

