from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('market.urls', namespace='market')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/register/", register, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
