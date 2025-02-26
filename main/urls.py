from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet
from .views import views_test
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


    

router = DefaultRouter()
router.register(r'tests', TestViewSet)



urlpatterns = [
    path('test/<int:test_id>/', views.start_test, name='start_test'), 
    path('section/<int:test_id>/', views.section_detail, name='section_detail'),
    path('create_test/', views.create_test, name='create_test'),
    path('delete_test/<int:test_id>/', views.delete_test, name='delete_test'),
    path('edit_test/<int:test_id>/', views.edit_test, name='edit_test'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),   
    path('chat/', views.chat, name='chat'),
    path('themes/', views.themes, name='themes'), 
    path('results/', views.results, name='results'),     
    path('results/<str:result_id>/', views.results, name='results'),
    path('test/people/', views.test_people, name='test_people'),
    path('test/time/', views.test_time, name='test_time'),
    path('test/world/', views.test_world, name='test_world'),
    path('test/material/', views.test_material, name='test_material'),
    path('test/imagination/', views.test_imagination, name='test_imagination'),
    path('', views.index, name='home'),
    path('about123', views.about, name='about'),
    path('log_in', views.log_in, name='log_in'),
    path('section/', views.section_list, name='section_list'),
    path('test/<int:test_id>/', views.start_test, name='start_test'),
    path('test/<int:test_id>/question/<int:question_id>/', views.question, name='question'),
    path('info', views.info, name='info'),
    path('test', include(router.urls)),
    path('theme1/', views.theme1, name='theme1'),
    path('theme2/', views.theme2, name='theme2'),
    path('theme3/', views.theme3, name='theme3'),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
