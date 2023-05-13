"""
URL configuration for testproject project.

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
from testapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('l/', views.create_child_left),
    path('r/', views.create_child_right),
    # path('m/', views.member_count),
    path('o/', views.commision_view),
    path('admin/', admin.site.urls),
    # path('reg/', views.user_tree),
    # path('parent/<int:parent_id>/', views.view_parent, name='view_parent'),
    path('', views.indexView),
    path('result/', views.searchView),
    path('parent/', views.parent_list),
    path('binary/', views.left_list),
    path('binary-right/', views.right_list),
    path('wallet/', views.walletView),
    path('kyc/', views.kyc),
    path('ticket/', views.ticketView),
    path('transcation/', views.transView),
    path('profile-detail/', views.showProfile),
    path('help/', views.helpView),
    path('profile-seetings/', views.profileSetting),
    path('table/', views.tableView), 
    path('accounts/login/', views.loginView, name='login'),
    path('signup/', views.signUpView),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
