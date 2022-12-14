from django.shortcuts import render
from django.views import generic
from .models import *


def main(request):
    folders = Folder.objects.filter(publicated=True, level=0)
    if request.GET.get('parent'):
        parent = request.GET.get('parent')
        level = int(request.GET.get('level')) + 1
        folders = Folder.objects.filter(parent_id=parent, level=level)

    context = {
        'folders': folders,
    }

    return render(request, 'Hujjatlar/index.html', context)


def creating(request):
    pass

    return render(request, 'Hujjatlar/creating.html')


def report(request, slug):
    reports = Report.objects.filter(department__slug=slug)
    current = ""
    print(reports.last())
    if reports.last() is not None:
        current = reports.last().url

    if request.GET.get("report_url"):
        current = Report.objects.filter(slug=request.GET.get("report_url"))
        current = current.first().url

    context = {
        'reports': reports,
        'current': current
    }

    return render(request, 'Hujjatlar/report.html', context)


def video_courses(request):
    pass

    return render(request, 'Hujjatlar/videoCourses.html')


def reals(request):
    pass

    return render(request, 'Hujjatlar/reals.html')
