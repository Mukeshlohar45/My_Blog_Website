"""myproject URL Configuration

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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loadhtml', views.loadhtml),
    path('', views.signup),
    path('savedata', views.savedata),
    path('login', views.login),
    path('register', views.register),
    path('home', views.home),
    path('About_us', views.About_us),
    path('Company', views.Company),
    path('sendEmail', views.sendEmail),
    path('Services', views.Services),
    path('logOut', views.logOut),
    path('webDesign', views.webDesign, name='webDesign'),
    path('javaScript', views.javaScript, name='javaScript'),
    path('Html', views.Html, name='Html'),
    path('Css', views.Css, name='Css'),
    path('Freebies', views.Freebies, name='Freebies'),
    path('Tutorials', views.Tutorials, name='Tutorials'),
    path('createpost', views.createpost),
    path('Visit', views.Visit)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
