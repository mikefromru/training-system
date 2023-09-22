from rest_framework import serializers
from .models import Lesson, LessonProduct, LessonScan, Product, ProductAccess


class ProductAccessSerializer(serializers.ModelSerializer):

    # name_ = serializers.PrimaryKeyRelatedField(read_only=True, source='name', allow_null=True, many=True)

    class Meta:

        model = ProductAccess
        fields = '__all__'
        # fields = ['name']
 
    # p = ProductSerializer(read_only=True, many=True, source='poduct.name')
    # products = ProductSerializer()
    # products = ProductAccessSerializer(read_only=True, many=True, source='product')
    # products = serializers.SerializerMethodField(read_only=True)
    # products_name = serializers.RelatedField(source='products.name', read_only=True)

#-----------------------------------

class ProductSerializer(serializers.ModelSerializer):

    # lessons = serializers.PrimaryKeyRelatedField(many=True, queryset=Lesson.objects.all())
    # print(lessons, ' <<<<< >>>>>')

    class Meta:

        model = Product
        fields = ['id', 'name', 'owner']


class LessonSerializer(serializers.ModelSerializer):

    products = ProductSerializer(read_only=True, many=True)
    # products = ProductSerializer()

    class Meta:
        
        model = Lesson
        fields = ('id', 'name', 'video_link', 'duration', 'products')
#-----------------------------------



class LessonScanSerializer(serializers.ModelSerializer):

    lesson = LessonSerializer()

    class Meta:

        model = LessonScan
        # fields = '__all__'
        fields = ('id', 'lesson', 'view_time', 'view_status')

