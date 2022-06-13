from django.contrib import admin
from .models import Video
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VideoResource(resources.ModelResource):

    class Meta:
        model = Video

@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin):
    pass
