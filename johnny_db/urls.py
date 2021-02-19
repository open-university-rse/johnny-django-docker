from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from website_activity.views import SearchViewSet, WebsiteActivityViewSet, WebsiteActivityAPIViewSet
from clipboard.views import ClipboardAPIViewSet

router = routers.DefaultRouter()
# router.register(r"searches", SearchViewSet, basename='Searches')
router.register(r"api/website", WebsiteActivityViewSet, basename='Website_activity')
router.register(r"api/clipboard", ClipboardAPIViewSet, basename='Clipboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('history', include('website_activity.urls')),
    path('clipboard', include('clipboard.urls')),
]
