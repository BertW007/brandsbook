"""brandsbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$',
        views.signup, name='signup'),
    url(r'^users/$',
        views.UserShowAllView.as_view(), name="user-show-all-view"),
    url(r'^login/',
        views.UserLoginView.as_view(), name="user-login"),
    url(r'^logout/',
        views.UserLogoutView.as_view(), name="user-logout"),
    url(r'^detail-user/(?P<pk>(\d)+)/$',
        views.UserDetailView.as_view(), name="user-detail"),
    url(r'^update-detail-user/(?P<pk>(\d)+)/$',
        views.UserUpdateDetailView.as_view(), name="user-update-detail"),
    url(r'^search/',
        views.SearchView.as_view(), name="search"),
    url(r'^$',
        views.HomeView.as_view(), name="home"),
    url(r'^brands/',
        views.BrandsAutocompleteView.as_view(), name="brands-search"),
    url(r'^add_brands/(?P<pk>(\d)+)/$',
        views.BrandsAddView.as_view(), name="brands-add"),
    url(r'^add_intbrands/(?P<pk>(\d)+)/$',
        views.InterestingBrandsAddView.as_view(), name="interesting-brands-add"),
    url(r'^cooperation/(?P<pk>(\d)+)/$',
        views.BrandsCooperationView.as_view(), name="cooperation"),
]
