from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('emissions.urls')),
    path('', lambda request: HttpResponse("Breathe ESG Dashboard is Live 🚀")),
]