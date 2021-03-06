from django.contrib import admin
from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('catalog/', views.catalog, name='catalog'),
    path('profilesoffered/', views.getProfilesOffered, name='ProfilesOffered'),
    path('register/<int:id>/', views.register_for_company, name='regcompany'),
    # path('logout/', views.logoutView, name='logout'),
]
