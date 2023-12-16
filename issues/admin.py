from django.contrib import admin
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = [
        "name","intro"

    ]
    admin.site.register(Status, StatusAdmin)
    admin.site.register(Issue)