from rest_framework import serializers
from .models import Lesson, LessonScan

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Lesson
        fields = '__all__'
        # fields = ('id', 'title', 'video_link', 'duration')

class LessonScanSerializer(serializers.ModelSerializer):

    lesson = LessonSerializer()

    class Meta:

        model = LessonScan
        fields = '__all__'
        # fields = ('id', 'lesson', 'view_time', 'view_status')