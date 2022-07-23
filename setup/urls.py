from django.contrib import admin
from django.urls import path, include

from rickandmorty.urls import router

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
