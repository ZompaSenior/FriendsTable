"""Friends App Models."""

# Standard Import

# Site-package Import
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local Import
from common import models as cm


class Friends(cm.Base, cm.EditInfo, cm.TrashBin):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = _("User"),
        help_text = _("User of this Friend"))
    
    image = models.ImageField(
        max_length = 255,
        blank = True,
        verbose_name = _("Profile Image"),
        help_text = _("The picture that is shown for the Friend"))
        