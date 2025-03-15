from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("trainees/", include("trainee.urls"), name="trainees"),
    path("courses/", include("course.urls"), name="courses")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
