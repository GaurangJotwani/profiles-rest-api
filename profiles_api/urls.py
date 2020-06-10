from django.urls import path, include
from .views import HelloApiView, HelloViewSet, UserProfileViewSet, UserLoginApiView, UserProfileFeedViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet)
router.register('feed', UserProfileFeedViewSet)


urlpatterns = [
    path('hello-view/', HelloApiView.as_view(), name='hello-api-view'),
    path('login/', UserLoginApiView.as_view(),),
    path('', include(router.urls))
]
