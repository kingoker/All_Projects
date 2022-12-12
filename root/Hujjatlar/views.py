from django.shortcuts import render
from django.views import generic
from .models import *


def main(request):
    folders = Folder.objects.filter(publicated=True)
    context = {
        'folders': folders,
    }

    return render(request, 'Hujjatlar/index.html', context)


def creating(request):
    pass

    return render(request, 'Hujjatlar/creating.html')


def report(request):
    pass

    return render(request, 'Hujjatlar/report.html')


def video_courses(request):
    pass

    return render(request, 'Hujjatlar/videoCourses.html')


def reals(request):
    pass

    return render(request, 'Hujjatlar/reals.html')