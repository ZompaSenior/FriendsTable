"""Friends Admin configuration."""

# Standard Import

# Site-package Import
from django.contrib import admin

# Project Import
from friend import models as fm

admin.site.register(fm.Friends)