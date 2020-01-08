from django.contrib import admin
from .models import inNeedOfService, serviceProvider

class HandyAdmin(admin.ModelAdmin):
    # class ProjectAdmin(ImportExportModelAdmin):
    list_display = ('id','manager', 'service_name', 'mycost')
    list_per_page = 5
    search_fields = ('manager', 'service_name', 'mycost')
    list_filter = ('manager', 'service_name', 'mycost')


# Register your models here.
admin.site.register(serviceProvider)
admin.site.register(inNeedOfService)


