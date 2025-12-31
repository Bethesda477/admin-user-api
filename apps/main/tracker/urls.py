from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_portal, name='user_portal'),
    path('admin/', views.admin_portal, name='admin_portal'),
    path('api/rows/', views.table_rows, name='table_rows'),
    path('api/admin-entries/', views.admin_entries_list, name='admin_entries_list'),
    path('api/edit/<int:pk>/', views.edit_entry, name='edit_entry'),
    path('api/delete/<int:pk>/', views.delete_entry, name='delete_entry'),
]