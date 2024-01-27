from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('home:home'), name='redirect-root'),
    path('api/', include(('API.urls', 'API'), namespace='api')),
    path('phone-list/', include(('home.urls', 'home'), namespace='home')),
]
