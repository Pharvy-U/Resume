from django.urls import path
from . import views


urlpatterns = [path('', views.resume, name='home'),
               path('send_email/', views.sendEmail, name='send_email')]
