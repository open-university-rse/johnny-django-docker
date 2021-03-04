from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from website_activity.views import WebsiteActivityViewSet, WebsiteActivityAPIViewSet
from clipboard.views import ClipboardAPIViewSet
from files.views import FilesAPIViewSet

router = routers.DefaultRouter()
router.register(r"api/website", WebsiteActivityViewSet, basename='Website_activity')
router.register(r"api/clipboard", ClipboardAPIViewSet, basename='Clipboard')
router.register(r"api/file", FilesAPIViewSet, basename='Files')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('history', include('website_activity.urls')),
    path('clipboard', include('clipboard.urls')),
    path('file', include('files.urls')),
]
