from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):

    facebook = models.URLField(blank=True, null=True, help_text="Facebook Page URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram Profile URL")
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn Profile URL")
    github = models.URLField(blank=True, null=True, help_text="Github URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("instagram"),
            FieldPanel("linkedin"),
            FieldPanel("github"),
        ],heading="Social Media Settings")
    ]