"""
URL configuration for LR7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.tables, name="home"),
    path('form_lawsuits/', views.form_lawsuits, name='lawsuit'),
    path('form_responsible/', views.form_responsible, name='responsible'),
    path('form_responsible_for_lawsuits/', views.form_responsible_for_lawsuits, name='responsible-lawsuit'),
    path('lawsuit/<int:pk>/',views.DetailViewLawsuit.as_view(), name='lawsuit-detail'),
    path('responsible/<int:pk>/',views.DetailViewResponsible.as_view(), name='responsible-detail'),
    path('responsible-lawsuit/<int:pk>/',views.DetailViewResponsible_lawsuit.as_view(), name='responsible_lawsuit-detail'),
    path('lawsuit/<int:pk>/update/', views.UpdateLawsuit.as_view(), name='lawsuit-update'),
    path('responsible/<int:pk>/update', views.UpdateResponsible.as_view(), name='responsible-update'),
    path('responsible-lawsuit/<int:pk>/update', views.UpdateResponsible_Lawsuit.as_view(), name='responsible_lawsuit-update'),
    path('lawsuit/<int:pk>/delete/', views.DeleteLawsuit.as_view(), name='lawsuit-delete'),
    path('responsible/<int:pk>/delete', views.DeleteResponsible.as_view(), name='responsible-delete'),
    path('responsible-lawsuit/<int:pk>/delete', views.DeleteResponsible_Lawsuit.as_view(), name='responsible_lawsuit-delete')
]
