from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import SpreadsheetModel
# Register your models here.

@admin.register(SpreadsheetModel)
class SpreadsheetAdmin(ImportExportModelAdmin):
    pass