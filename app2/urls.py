from django.urls import path

from app2 import views

urlpatterns = [

    path("student/", views.StudentAPIView.as_view()),
    path("student/<str:pk>/", views.StudentAPIView.as_view()),
]