from django.contrib import admin
from adminsortable.admin import SortableAdmin

from .models import Profile, Subject, Language, OperatingSystem, Tool, \
    Certification, Education, Experience, Technology, Responsibility, Software, Project, Contact


class MySortableAdminClass(SortableAdmin):
    """Any admin options you need go here"""

admin.site.register(Profile, MySortableAdminClass)
admin.site.register(Subject, MySortableAdminClass)
admin.site.register(Language, MySortableAdminClass)
admin.site.register(OperatingSystem, MySortableAdminClass)
admin.site.register(Tool, MySortableAdminClass)
admin.site.register(Certification, MySortableAdminClass)
admin.site.register(Education, MySortableAdminClass)
admin.site.register(Experience, MySortableAdminClass)
admin.site.register(Technology, MySortableAdminClass)
admin.site.register(Responsibility, MySortableAdminClass)
admin.site.register(Software, MySortableAdminClass)
admin.site.register(Project, MySortableAdminClass)
admin.site.register(Contact, MySortableAdminClass)

