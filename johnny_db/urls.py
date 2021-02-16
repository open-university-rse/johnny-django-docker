from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from website_activity.views import SearchViewSet, WebsiteActivityViewSet, WebsiteActivityAPIViewSet, WebsiteActivityAPIViewSet
import debug_toolbar

router = routers.DefaultRouter()
router.register(r"searches", SearchViewSet, basename='Searches')
router.register(r"websites", WebsiteActivityViewSet, basename='Website_activity')
# router.register(r"websites", WebsiteActivityAPIViewSet, basename='Website_activity')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('__debug__/', include(debug_toolbar.urls)),
]
