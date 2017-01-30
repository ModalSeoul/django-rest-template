from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from apps.user.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
