from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Grade(models.Model):
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.grade


class Subject(models.Model):
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, blank=True, null=True)
    subject_name = models.CharField(max_length=200)
    syllabus = RichTextField()

    def __str__(self):
        return self.subject_name


class ImageVideo(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True, null=True)
    small_desc = models.CharField(max_length=200, default="0")
    file_name = models.CharField(max_length=255)
    your_image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return self.file_name



class GradeComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment + " - By " + self.user.username
