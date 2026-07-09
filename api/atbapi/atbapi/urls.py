"""
URL configuration for atbapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

#для картинок на фронті
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #сканує всі ViewSet'и, серіалізатори, роутери й генерує openapi.yaml/JSON схему автоматично (аналог того, що Swashbuckle робить в ASP.NET, читаючи атрибути контролерів
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    #бере цю схему і рендерить інтерактивний UI (Swagger UI), де можна тестувати ендпоінти прямо з браузера.
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include('users.urls'))
]

#якщо DEBUG=False Тоді Django не повинен віддавати статичні чи медіафайли. Цим займається Nginx, Apache або інший вебсервер.
if settings.DEBUG:
    urlpatterns += static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)