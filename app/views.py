from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Lesson, LessonScan
from .serializers import LessonSerializer, LessonScanSerializer
from rest_framework import permissions

class LessonListView(ListAPIView):

    serializer_class = LessonScanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        products = user.productaccess_set.all().values_list('product', flat=True)
        lessons = Lesson.objects.filter(products__in=products).distinct()
        lesson_view = LessonScan.objects.filter(user=user, lesson__in=lessons)
        return lesson_view


