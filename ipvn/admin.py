from django.contrib import admin
from .models import IpRange


class IpRangeAdmin(admin.ModelAdmin):
    list_display = ('from_ip', 'to_ip')


admin.site.register(IpRange, IpRangeAdmin)