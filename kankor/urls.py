
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from .import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_panel.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
