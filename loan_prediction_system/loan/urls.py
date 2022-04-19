from django.urls import path, include
from .views import GetResult

urlpatterns = [
    path("", GetResult.as_view()),
]