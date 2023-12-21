"""
URL configuration for guidebook project.

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
from django.contrib import admin
from django.urls import path

from users.views import IndexView, SearchView, AddRecordView, EditRecordView, IndexSurnameView, EditRecordSurnameView, AddRecordSurnameView, IndexFirstnameView, EditRecordFirtnameView, AddRecordFirstnameView, IndexPatronymicView, EditRecordPatronymicView, AddRecordPatronymicView, IndexStreetView, EditRecordStreetView, AddRecordStreetView, delete_record, delete_record_surname, delete_record_firstname, delete_record_patronymic, delete_record_street


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('surnames/', IndexSurnameView.as_view(), name='surnames'),
    path('firstnames/', IndexFirstnameView.as_view(), name='firstnames'),
    path('patronymics/', IndexPatronymicView.as_view(), name='patronymics'),
    path('streets/', IndexStreetView.as_view(), name='streets'),
    path('search/', SearchView.as_view(), name='search'),
    path('search/result', SearchView.as_view(template_name='search_result.html'),
         name='search_result'),
    path('delete/<int:pk>/', delete_record, name='delete_record'),
    path('delete_surname/<int:pk>/', delete_record_surname,
         name='delete_record_surname'),
    path('delete_firstname/<int:pk>/', delete_record_firstname,
         name='delete_record_firstname'),
    path('delete_patronymic/<int:pk>/', delete_record_patronymic,
         name='delete_record_patronymic'),
    path('delete_street/<int:pk>/', delete_record_street,
         name='delete_record_street'),
    path('add_record/', AddRecordView.as_view(), name='add_record'),
    path('add_record_surname/', AddRecordSurnameView.as_view(),
         name='add_record_surname'),
    path('add_record_firstname/', AddRecordFirstnameView.as_view(),
         name='add_record_firstname'),
    path('add_record_patronymic/', AddRecordPatronymicView.as_view(),
         name='add_record_patronymic'),
    path('add_record_street/', AddRecordStreetView.as_view(),
         name='add_record_street'),
    path('edit_record/<int:pk>/', EditRecordView.as_view(), name='edit_record'),
    path('edit_record_surname/<int:pk>/',
         EditRecordSurnameView.as_view(), name='edit_record_surname'),
    path('edit_record_firtname/<int:pk>/',
         EditRecordFirtnameView.as_view(), name='edit_record_firstname'),
    path('edit_record_patronymic/<int:pk>/',
         EditRecordPatronymicView.as_view(), name='edit_record_patronymic'),
    path('edit_record_street/<int:pk>/',
         EditRecordStreetView.as_view(), name='edit_record_street'),



]
