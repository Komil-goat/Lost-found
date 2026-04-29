from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404) 

def custom_500(request):
    return render(request, '500.html', status=500)

handler404 = 'lost_and_found.urls.custom_404'
handler500 = 'lost_and_found.urls.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', include('home.urls')),
    path('items/', include('items.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)