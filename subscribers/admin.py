from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from .models import Subscribers

class SubscriberAdmin(ModelAdmin):
    model = Subscribers
    menu_label = "Subscribers"
    menu_icon = "mail"
    menu_order = 5
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email", "full_name",)
    search_fields = ("email", "full_name",)

modeladmin_register(SubscriberAdmin)