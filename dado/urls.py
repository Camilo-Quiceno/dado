
from django.contrib import admin
from django.urls import include,path

from django.config import settings
from django.config.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lanzamiento/', include(('lanzamiento.urls','lanzamiento'), namespace = 'lanzamiento')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
