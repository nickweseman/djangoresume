from django.db import models
from adminsortable.models import SortableMixin


class Technology(SortableMixin):
    name = models.CharField(max_length=300)
    icon = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name


class Profile(SortableMixin):
    website = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    icon = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.website


class Subject(SortableMixin):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name


class Language(SortableMixin):
    technology = models.OneToOneField(Technology, on_delete=models.CASCADE,
                                      default=1, primary_key=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.technology.name


class OperatingSystem(SortableMixin):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name


class Tool(SortableMixin):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name


class Certification(SortableMixin):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name


class Education(SortableMixin):
    school = models.CharField(max_length=300)
    degree = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    gpa = models.CharField(max_length=100)
    graduation_date = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.school


class Experience(SortableMixin):
    company = models.CharField(max_length=300)
    url = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=100)
    years = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.company


class Project(SortableMixin):
    experience = models.ForeignKey('resume.Experience', related_name='projects')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    years = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name


class Responsibility(SortableMixin):
    project = models.ForeignKey('resume.Project', related_name='responsibilities',
                                blank=True, null=True)
    experience = models.ForeignKey('resume.Experience', related_name='responsibilities',
                                   blank=True, null=True)
    software = models.ForeignKey('resume.Software', related_name='responsibilities',
                                 blank=True, null=True)
    description = models.TextField(max_length=500)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.description


class Software(SortableMixin):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    icon = models.CharField(max_length=300, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)

    class Meta:
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name
