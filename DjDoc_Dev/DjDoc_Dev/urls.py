from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('DjDoc_App.urls')),
    path('rest/', include('DjDoc_Rest.urls')),
]
