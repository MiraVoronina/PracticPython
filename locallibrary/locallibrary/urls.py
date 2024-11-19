# locallibrary/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),  # Подключение URL-ов приложения catalog
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),  # Редирект на страницу с книгами
]
