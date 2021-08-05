from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('services/',views.services,name="services"),
    path('process/',views.process,name="process"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
]
