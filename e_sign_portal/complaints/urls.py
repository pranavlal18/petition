from django.urls import path
from . import views
from .views import my_petitions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.petition_list, name='petition_list'),
    path('create/', views.create_petition, name='create_petition'),
    path('sign/<int:petition_id>/', views.sign_petition, name='sign_petition'),
    path('about/', views.about, name='about'),
    path('contact/', views.contract, name='contact'),
    path('petition/<int:petition_id>/', views.petition_detail, name='petition_detail'),
    path('petition/<int:petition_id>/edit/', views.edit_petition, name='edit_petition'),
    path('my_petitions/', my_petitions, name='my_petitions'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
