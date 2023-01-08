from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . models import *


class FolderAdmin(MPTTModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class ReportAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Folder, FolderAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Report, ReportAdmin)

