from django.urls import path, include

urlpatterns = [
    path('api/', include('app.urls')),  # app_name ni loyihangiz nomiga almashtiring
]
