from .models import *


def default(request):
    departments = Department.objects.all

    return {
        'departments': departments,
    }