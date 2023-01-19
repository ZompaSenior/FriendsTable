"""Restaurant App Models."""

# Standard Import

# Site-package Import
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local Import
from common import models as cm


class Restaurant(cm.Base, cm.EditInfo, cm.TrashBin):
    image = models.ImageField(
        max_length = 255,
        blank = True,
        verbose_name = _("Restaurant Logo"),
        help_text = _("The logo picture of the restaurant"))


class MenuEntry(cm.Base, cm.EditInfo, cm.TrashBin, cm.Ordered):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete = models.CASCADE,
        related_name = "menu_entries",
        verbose_name = _("Restaurant"),
        help_text = _("The Restaurant owner of this Menu Entry"))
    
    image = models.ImageField(
        max_length = 255,
        blank = True,
        verbose_name = _("Dish Image"),
        help_text = _("The picture of the current dish"))
    
    max = models.SmallIntegerField(
        default = 0,
        verbose_name = _("Max"),
        help_text = _("Max quantity of portions it is possible to order"))
    
    
    