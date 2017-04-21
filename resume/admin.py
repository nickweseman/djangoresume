from django.contrib import admin

from .models import Profile, Subject, Language, OperatingSystem, Tool, \
    Certification, Education, Experience, Technology, Responsibility, Software

admin.site.register(Profile)
admin.site.register(Subject)
admin.site.register(Language)
admin.site.register(OperatingSystem)
admin.site.register(Tool)
admin.site.register(Certification)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Technology)
admin.site.register(Responsibility)
admin.site.register(Software)
