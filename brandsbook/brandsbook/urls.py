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
    url(r'^users',
        views.UserShowAllView.as_view(), name="user-show-all-view"),
    url(r'^create-user/',
        views.UserCreateView.as_view(), name="user-create-view"),
    url(r'^login/',
        views.UserLoginView.as_view(), name="user-login"),
    url(r'^logout/',
        views.UserLogoutView.as_view(), name="user-logout"),
    url(r'^add-user/',
        views.UserCreateView.as_view(), name="user-create"),
    url(r'^deatil-user/(?P<pk>(\d)+)',
        views.UserDetailView.as_view(), name="user-detail"),
    url(r'^update-user/(?P<pk>(\d)+)',
        views.UserUpdateView.as_view(), name="user-update"),
    url(r'^search/',
        views.SearchView.as_view(), name="search"),
    url(r'^home/',
        views.HomeView.as_view(), name="home"),
    url(r'^brands/',
        views.BrandsAutocompleteView.as_view(), name="brands-search"),
    url(r'^fav-brands/',
        views.BrandsFavView.as_view(), name="brands-fav"),
    url(r'^msgs/',
        views.UserMsgView.as_view(), name="msgs"),
    url(r'^cooperation/',
        views.BrandsCooperationView.as_view(), name="cooperation"),
]
