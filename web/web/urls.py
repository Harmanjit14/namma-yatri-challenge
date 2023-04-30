"""
URL configuration for web project.

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
from answer import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('answer/', views.answer, name='answer-call-server'),
    path('test/', views.test, name='dummy-url-server'),
    path('book-auto/',views.book_auto,name='book-auto'),
    path('hangup-call/',views.hangup, name='hangup-call-server')
]


urlpatterns +=[
    path('sms/', views.reply_sms, name='inbound-sms'),
    path('sms-failiure/', views.reply_sms_fail, name='inbound-sms-fail'),
]

urlpatterns+=[
    path('get-user/',views.get_user,name="get-user"),
    path('get-location/',views.get_location,name='get-Location'),
    path('test-data/',views.test_data,name='test-data')
]