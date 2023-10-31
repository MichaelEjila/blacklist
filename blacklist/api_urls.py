from rest_framework.routers import DefaultRouter
from django.urls import path, include
from main.endpoints.views import DataTypeViewSet, FlaggedDataViewSet

router = DefaultRouter()
router.register(r'datatype', DataTypeViewSet, basename='datatype')
router.register(r'flaggeddata', FlaggedDataViewSet, basename='flaggeddata')

urlpatterns = [
    path('', include(router.urls)),
]