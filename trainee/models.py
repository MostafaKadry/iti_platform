from django.db import models
from course.models import Course
import os

# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    @classmethod
    def add_trainee(cls, name, email, phone, address, image, course):
        Trainee.objects.create(name=name, email=email, phone=phone,address=address ,image=image, course=course)

    @classmethod
    def update_trainee(cls, trainee_id, name, email, phone, address, image, course):
        cls.objects.filter(id=trainee_id).update(
            name=name,
            email=email,
            phone=phone,
            address=address,
            image=image,
            course=course
        )
    @classmethod
    def get_trainee_by_id(cls, trainee_id):
        return cls.objects.get(id=trainee_id)

    def save(self, *args, **kwargs):
        if self.pk:
            old_profile = Trainee.objects.filter(pk=self.pk).first()
            if old_profile and old_profile.image and old_profile.image != self.image:
                old_image_path = os.path.join(old_profile.image.path)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
