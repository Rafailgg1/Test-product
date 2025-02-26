from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_home, name='test_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.TestDetailView.as_view(), name='test-detail'),
    path('<int:pk>/update', views.TestUpdateView.as_view(), name='test-update'),
    path('<int:pk>/delete', views.TestDeleteView.as_view(), name='test-delete')
]   
