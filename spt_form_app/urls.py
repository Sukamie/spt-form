"""
URL configuration for spt_form_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from tkinter.font import names

from django.contrib import admin
from django.urls import path

from spt_form_app.views import form_01a, export_form_01c, delete_form_01c, edit_form_01c
from spt_form_app.views import form_01b
from spt_form_app.views import form_01c
from spt_form_app.views import form_spt_1111
from spt_form_app.views import home

from spt_form_app.views import form_01a_manage
from spt_form_app.views import form_01b_manage
from spt_form_app.views import form_01c_manage
from spt_form_app.views import form_spt_1111_manage

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('create/form-01a', form_01a, name='form-01a'),
    path('create/form-01b', form_01b, name='form-01b'),
    path('create/form-01c', form_01c, name='form-01c'),
    path('create/form-spt-1111', form_spt_1111, name='form-spt-1111'),

    # Form Manage
    path('form_manage/form_01a', form_01a_manage, name='form_01a_manage'),
    path('form_manage/form_01b', form_01b_manage, name='form_01b_manage'),
    path('form_manage/form_01c', form_01c_manage, name='form_01c_manage'),
    path('form_manage/form_spt_1111', form_spt_1111_manage, name='form_spt_1111_manage'),

    # Form Delete
    path('delete-form-01c/<int:form_id>/', delete_form_01c, name='delete_form_01c'),

    # Form Edit
    path('edit-form-01c/<int:form_id>', edit_form_01c, name='edit_form_01c'),

    # Form Export
    path('export-form-01c/<int:form_id>/', export_form_01c, name='export_form_01c'),

]
