from django.contrib import admin
from main.models import FlaggedData, DataType

# Register your models here.
admin.site.register(FlaggedData)
admin.site.register(DataType)