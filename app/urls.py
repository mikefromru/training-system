from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.LessonListView().as_view(), name='lesson-list'),
]

