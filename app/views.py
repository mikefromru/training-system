from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Lesson, LessonScan, Product, ProductAccess
from .serializers import LessonSerializer, LessonScanSerializer, ProductSerializer
from rest_framework import permissions


class LessonListView(ListAPIView):

    serializer_class = LessonScanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        lesson_view = LessonScan.objects.filter(user=user)
        return lesson_view
    


