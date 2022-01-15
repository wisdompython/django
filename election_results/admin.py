from django.contrib import admin
from .models import AnnouncedPuResults,AnnouncedWardResults,AnnouncedStateResults,AnnouncedLgaResults,Agentname,New_Polling_unit

# Register your models here.
admin.site.register(Agentname)
admin.site.register(AnnouncedLgaResults)
admin.site.register(AnnouncedPuResults)
admin.site.register(New_Polling_unit)


