"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import include, path

urlpatterns = [
    path('index/', views.index, name='main-view'),
    path('bio/<username>/', views.bio, name='bio'),
    path('articles/<slug:title>/', views.article, name='article-detail'),
    path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
    path('weblog/', include('blog.urls')),
    ...
]

"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^$',views.HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^test/$',views.TestPage.as_view(),name='test'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^groups/',include('groups.urls',namespace='groups')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    
    #new way to use path & include
    # path('community/', include('aggregator.urls')),
    # path('contact/', include('contact.urls')),
    # path('', views.index, name='index'),


    # url(r'^$',views.HomePage.as_view(), name='home'),
    # url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    # url(r'^accounts/',include('django.contrib.auth.urls')),
    # url(r'^test/$',views.TestPage.as_view(),name='test'),
    # url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    # url(r'^posts/',include('posts.urls',namespace='posts')),
    # url(r'^groups/',include('groups.urls',namespace='groups')),