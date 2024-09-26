from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('items/', include('items.urls')),
    path('equipment/', include('equipment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
