from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', lambda request: HttpResponse("Hi, this is Purva")),  # Add this line for direct text response
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
