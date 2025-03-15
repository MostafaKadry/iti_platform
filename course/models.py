from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    @staticmethod
    def get_all_courses():
       return Course.objects.all().values()

    @classmethod
    def get_course_by_id(cls, id):
        return Course.objects.get(id=id)
    def __str__(self):
        return self.name