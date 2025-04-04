"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('getting_data',views.getting_data,name='getting_data'),
    path('sending_data',views.sending_data,name='sending_data'),
    path('updating/<int:id>',views.updating,name='updating'),
    path('dele',views.dele,name='dele'),
]
