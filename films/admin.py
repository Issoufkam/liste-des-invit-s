from django.contrib import admin
from .models import Invite

# Register your models here.
class InviteAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenoms", "table", "numero")
admin.site.register(Invite, InviteAdmin)
