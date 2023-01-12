"""Table App Models."""

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


class Table(cm.Base, cm.EditInfo, cm.TrashBin):
    """The Table of Friends at the Restaurant."""
    
    reservation_date = models.DateTimeField(
        auto_now = False,
        auto_now_add = False,
        default = now,
        verbose_name = _("reservation Date and Time"),
        help_text = _("The Date and Time of the table reservation"))

    diners = models.ManyToManyField(
        fm.Friends,
        verbose_name = _("Diners"),
        help_text = _("List of diners at the Table"),
        related_name = 'tables')
    
    restaurant = models.ForeignKey(
        rm.Restaurant,
        on_delete = models.CASCADE,
        related_name = "reserved_tables",
        verbose_name = _("Restaurant"),
        help_text = _("The Restaurant at witch the Table is reserved"))
    
    

    