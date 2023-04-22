from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^cifar-admin/', admin.site.urls),
    url(r'^', include('main.urls')),
]


urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
