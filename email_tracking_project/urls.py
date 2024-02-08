# email_tracking_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('em/', include('email_tracking_app.urls')),
    path('api/', include('email_tracking_app.urls')),
    # Add other URL patterns as needed
]
