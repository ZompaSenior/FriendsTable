"""Restaurants Admin configuration."""

# Standard Import

# Site-package Import
from django.contrib import admin

# Project Import
from restaurant import models as rm

admin.site.register(rm.Restaurant)
admin.site.register(rm.MenuEntry)