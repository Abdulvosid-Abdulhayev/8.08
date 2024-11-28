from django.urls import path
from .views import FoodTypeView,FoodTypeDetailView, FoodView,FoodDetailView, CommentView, CommentDetailView

urlpatterns = [
    path('food-types/', FoodTypeView.as_view(), name='foodtype-list'),
    path('food-types/<int:pk>/', FoodTypeDetailView.as_view(), name='foodtype-detail'),
    path('foods/', FoodView.as_view(), name='food-list'),
    path('foods/<int:pk>/', FoodDetailView.as_view(), name='food-detail'),
    path('comments/', CommentView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
