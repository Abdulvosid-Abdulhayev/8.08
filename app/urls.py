from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodTypeViewSet, FoodViewSet, CommentViewSet, SendEmailView

# Router yaratish
router = DefaultRouter()
router.register(r'foodtypes', FoodTypeViewSet, basename='foodtype')
router.register(r'foods', FoodViewSet, basename='food')
router.register(r'comments', CommentViewSet, basename='comment')

# URLS
urlpatterns = [
    path('', include(router.urls)),  # ViewSetlar uchun router URL
    path('send-email/', SendEmailView.as_view(), name='send_email'),  # Email uchun alohida URL
]
