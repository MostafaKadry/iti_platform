from django.db import models
from course.models import Course
import os
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class Trainee(models.Model):
    username = models.CharField(max_length=70, unique=True, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    @classmethod
    def add_trainee(cls, username, email, phone, address, image, course, password):
        Trainee.objects.create(username=username, email=email, phone=phone,address=address ,image=image, course=course, password=password)

    @classmethod
    def update_trainee(cls, trainee_id, username, email, phone, address, image, course):
        cls.objects.filter(id=trainee_id).update(
            username=username,
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
        #Update Existing Trainee, remove old image
        if self.pk:
            old_profile = Trainee.objects.filter(pk=self.pk).first()
            if old_profile and old_profile.image and old_profile.image != self.image:
                old_image_path = os.path.join(old_profile.image.path)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)

        # Create new Trainee, Hash password before saving
        if not self.pk or not Trainee.objects.filter(pk=self.pk).exists():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.username}"
