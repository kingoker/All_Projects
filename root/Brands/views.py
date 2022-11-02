from django.shortcuts import render

from Brands.models import *


def main(request):
    manufacture = Manufacture.objects.all()

    data = {
        'manufacture': manufacture,
    }
    
    return render(request, 'Brands/index.html', data)