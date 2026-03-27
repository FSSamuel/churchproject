from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('visit/', views.visit, name='visit'),
    path('contact/', views.contact, name='contact'),
    path('english/', views.english, name='english'),
    path('cantonese/', views.cantonese, name='cantonese'),
    path('get-connected/', views.get_connected, name='get_connected'),
    path('serve-others/', views.serve_others, name='serve_others'),
]


urlpatterns += staticfiles_urlpatterns()
