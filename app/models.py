from django.db import models
from django.contrib.auth.models import User

class FoodType(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi


class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name="foods")
    nomi = models.CharField(max_length=100)
    tarkibi = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nomi


class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.food.nomi}"
