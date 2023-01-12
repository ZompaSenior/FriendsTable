"""Tables Admin configuration."""

# Standard Import

# Site-package Import
from django.contrib import admin

# Project Import
from table import models as tm

admin.site.register(tm.Table)