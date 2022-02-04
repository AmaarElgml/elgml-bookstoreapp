"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from storeapp import views
from storeapp.views import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1 GET and POST Authors
    # path('authors/', views.AuthorListGenerics.as_view()),

    # 2 GET, PUT, and DELETE Authors
    # path('authors/<int:pk>', views.AuthorPKGenerics.as_view()),

    # 3 GET and POST Books
    # path('books/', views.BooksListGenerics.as_view()),

    # 4 GET, PUT, and DELETE Books
    # path('books/<int:pk>', views.BooksPKGenerics.as_view()),

    # 5 GET and POST News
    path('data/', include(router.urls)),

    # 6 GET, PUT, and DELETE News
    # path('news/<int:pk>', views.NewsPKGenerics.as_view()),

    # 7 GET and POST AppAdmins
    # path('appadmins/', views.AppAdminListGenerics.as_view()),

    # 8 GET, PUT, and DELETE AppAdmins
    # path('appadmins/<int:pk>', views.AppAdminPKGenerics.as_view()),
]
