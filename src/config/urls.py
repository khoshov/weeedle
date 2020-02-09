from django.contrib import admin
from django.urls import path, include, re_path

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('censorship/', include('censorship.urls', namespace='censorship')),
    path('', include('strains.urls', namespace='strains')),
]

if settings.DEBUG:
    from django.views.static import serve

    urlpatterns += [
        re_path(
            r'^media/(?P<path>.*)$', serve, kwargs={'document_root': settings.MEDIA_ROOT}
        ),
        re_path(
            r'^static/(?P<path>.*)$', serve, kwargs={'document_root': settings.STATIC_ROOT}
        ),
    ]
