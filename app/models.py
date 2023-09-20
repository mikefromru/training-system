from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductAccess(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

#
class Lesson(models.Model):

    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name

class LessonProduct(models.Model):

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

#
class LessonScan(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    viewed_time = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.viewed_time >= self.lesson.duration * 0.8:
            self.viewed = True
        super().save(*args, **kwargs)