from django.contrib import admin
from .models import Agent, Software, SystemSnapshot, SnapshotSoftware

admin.site.register(Agent)
admin.site.register(Software)
admin.site.register(SystemSnapshot)
admin.site.register(SnapshotSoftware)