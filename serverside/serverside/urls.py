from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('detection.urls')),
    re_path(r'^api/', include(('alertupload_rest.urls', 'alertupload_rest'), namespace='api')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
