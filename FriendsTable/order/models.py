"""Order App Models."""

# Standard Import

# Site-package Import
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from  django.utils.timezone import now

# Local Import
from common import models as cm
from friend import models as fm
from restaurant import models as rm
from table import models as tm


class Order(cm.EditInfo, cm.TrashBin):
    """The Order of the single Friend in the Table."""
    
    id = models.AutoField(primary_key = True)
    
    table = models.ForeignKey(
        tm.Table,
        on_delete = models.CASCADE,
        related_name = "table_orders",
        verbose_name = _("Table"),
        help_text = _("The Table of the Order"))
    
    menu_entry = models.ForeignKey(
        rm.MenuEntry,
        on_delete = models.CASCADE,
        related_name = "entry_orders",
        verbose_name = _("Menu Entry"),
        help_text = _("The Menu Entry of the Order"))
    
    quantity = models.SmallIntegerField(
        default = 0,
        verbose_name = _("Quantity"),
        help_text = _("The Quantity of the Order"))
    
    friend = models.ForeignKey(
        fm.Friends,
        blank = True,
        on_delete = models.CASCADE,
        related_name = "friend_orders",
        verbose_name = _("Diner"),
        help_text = _("The Diner owner of the Order"))
    
    def __str__(self):
        return f"{self.table} - {self.friend} - {self.menu_entry} - {self.quantity}"

    
    
    