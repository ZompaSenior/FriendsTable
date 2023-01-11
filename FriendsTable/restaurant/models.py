"""Restaurant App Models."""

# Standard Import

# Site-package Import
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local Import
from common import models as cm


class Restaurant(cm.Base, cm.EditInfo, cm.TrashBin):
    pass

class MenuEntry(cm.Base, cm.EditInfo, cm.TrashBin):
    models.ForeignKey(
        Restaurant,
        on_delete = models.CASCADE,
        related_name = "menu_entries",
        verbose_name = _("Restaurant"),
        help_text = _("The Restaurant owner of this Menu Entry"))
    
    