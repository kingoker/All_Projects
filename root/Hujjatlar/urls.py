from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('creating', views.creating, name='creating'),
    path('report/<slug:slug>', views.report, name='report'),
    path('videoCourses', views.video_courses, name='videoCourses'),
    path('reals', views.reals, name='reals'),
]