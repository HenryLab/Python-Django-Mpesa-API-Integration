from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    division_by_zero = 300 / 0


urlpatterns = [
    path('api/v1/', include('mpesa_api.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug', trigger_error),
]
