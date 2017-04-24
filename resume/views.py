from django.shortcuts import render

from resume.models import Profile, Subject, Language, OperatingSystem, \
    Tool, Certification, Education, Experience, Project, Technology, Responsibility, Software


def resume(request):
    return render(request, 'resume/index.html', {'profiles': Profile.objects.all(),
                                                 'subjects': Subject.objects.all(),
                                                 'languages': Language.objects.all(),
                                                 'operating_systems': OperatingSystem.objects.all(),
                                                 'tools': Tool.objects.all(),
                                                 'certifications': Certification.objects.all(),
                                                 'educations': Education.objects.all(),
                                                 'experiences': Experience.objects.all(),
                                                 'projects': Project.objects.all(),
                                                 'technologies': Technology.objects.all(),
                                                 'responsibilities': Responsibility.objects.all(),
                                                 'softwares': Software.objects.all()})
