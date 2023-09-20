from django.contrib import admin
from .models import ( 
                    Product, 
                    ProductAccess,
                    Lesson,
                    LessonProduct,
                )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    pass

@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):

    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    pass

@admin.register(LessonProduct)
class LessonProductAdmin(admin.ModelAdmin):

    pass

