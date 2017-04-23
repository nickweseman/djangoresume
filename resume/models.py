from django.db import models


class Profile(models.Model):
    website = models.CharField(max_length=100)
    url = models.TextField(max_length=300)
    icon = models.CharField(max_length=100, null=True)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=300, null=True)


class Language(models.Model):
    pass  # see Technology


class OperatingSystem(models.Model):
    name = models.CharField(max_length=100)


class Tool(models.Model):
    name = models.CharField(max_length=100)


class Certification(models.Model):
    name = models.CharField(max_length=100)


class Education(models.Model):
    school = models.CharField(max_length=300)
    degree = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    gpa = models.CharField(max_length=100)
    graduation_date = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=500, null=True)


class Experience(models.Model):
    company = models.CharField(max_length=300)
    url = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=100)
    years = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    title = models.CharField(max_length=100, null=True)
    icon = models.CharField(max_length=100, null=True)


class Project(models.Model):
    experience = models.ForeignKey('resume.Experience', related_name='projects')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300, null=True)
    description = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=100, null=True)
    years = models.CharField(max_length=100, null=True)


class Technology(models.Model):
    project = models.ForeignKey('resume.Project', related_name='technologies')
    experience = models.ForeignKey('resume.Experience', related_name='technologies')
    education = models.ForeignKey('resume.Education', related_name='technologies')
    software = models.ForeignKey('resume.Software', related_name='technologies')
    language = models.ForeignKey('resume.Language', related_name='technologies')
    name = models.CharField(max_length=300)
    icon = models.CharField(max_length=100, null=True)


class Responsibility(models.Model):
    project = models.ForeignKey('resume.Project', related_name='responsibilities')
    experience = models.ForeignKey('resume.Experience', related_name='responsibilities')
    software = models.ForeignKey('resume.Software', related_name='responsibilities')
    description = models.TextField(max_length=500)


class Software(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    icon = models.CharField(max_length=300, null=True)
    url = models.CharField(max_length=500, null=True)
