from django.urls import path, include
#from merger import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("", include("merger.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)