from django.db import models
from django.contrib.auth.models import User


class FalbertUser(User):
    net_id = models.CharField(max_length=20, blank=True)
    courses_taken = models.ManyToManyField("Class", related_name="courses")
    interested_classes = models.ManyToManyField("Class", related_name='class_followers')
    current_class_schedule = models.ManyToManyField("Class", related_name='students')
    current_class_schedule_confirmed = models.BooleanField(default=False)
    major = models.ManyToManyField("Major", related_name='students')

    def import_from_dict(self, dict):
        #validate dict
        #adding info
        pass #STUB


class Major(models.Model):
    major_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    requirements = models.ManyToManyField("Course", related_name='+')

class Course(models.Model):
    course_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    is_offering = models.BooleanField(default=None)

class Class(models.Model):
    class_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    parent_course = models.ForeignKey("Course")
    is_open = models.BooleanField(default=None)
    format = models.CharField(max_length=20)
    time = models.TimeField()
    rmp_link = models.URLField()





