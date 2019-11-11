"""contest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from .views import (
    contest_post_create_view,
    contest_post_delete_view,
    contest_post_detail_view,
    contest_post_list_view,
    contest_post_update_view,
    category_crud_post_view,
    category_post_list_view,
    team_list_post_view,
    team_crud_post_view,
    team_post_detail_view,
    team_post_delete_view,
    person_list_view,
    person_crud_view,
)


urlpatterns = [
	path('', contest_post_list_view),
    path('admin/', admin.site.urls),

    path('contest-list/', contest_post_list_view),
    path('contest-new/', contest_post_create_view),

    path('contest/<str:slug>/', contest_post_detail_view),
    path('contest/<str:slug>/update/', contest_post_update_view),
    path('contest/<str:slug>/delete/', contest_post_delete_view),

    path('contest/<str:slug>/category-new/', category_crud_post_view),
    path('contest/<str:slug>/category-list/', category_post_list_view),

    path('contest/<str:slug>/team-list/', team_list_post_view),
    path('contest/<str:slug>/team-new/', team_crud_post_view),

    path('contest/<str:slug>/team/<int:pk>/', team_post_detail_view),
    path('contest/<str:slug>/team/<int:pk>/delete/', team_post_delete_view),

    path('contest/<str:slug>/team/<int:pk>/person-list/', person_list_view),
    path('contest/<str:slug>/team/<int:pk>/person-new/', person_crud_view),
]
