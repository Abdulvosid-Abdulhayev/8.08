from django.urls import path
from .views import FoodTypeView, FoodView, CommentView

urlpatterns = [
    path('food-types/', FoodTypeView.as_view(), name='foodtype-list'),
    path('food-types/<int:pk>/', FoodTypeView.as_view(), name='foodtype-detail'),
    path('foods/', FoodView.as_view(), name='food-list'),
    path('foods/<int:pk>/', FoodView.as_view(), name='food-detail'),
    path('comments/', CommentView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentView.as_view(), name='comment-detail'),
]
