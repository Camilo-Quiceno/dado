
from django.contrib import admin
from django.urls import include,path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lanzamiento/', include(('lanzamiento.urls','lanzamiento'), namespace = 'lanzamiento')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
