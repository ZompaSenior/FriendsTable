"""Orders Admin configuration."""

# Standard Import

# Site-package Import
from django.contrib import admin

# Project Import
from order import models as om

admin.site.register(om.Order)
