from django.db import models
from django.contrib.auth.models import User
from twilio.rest import TwilioRestClient
import re

class FalbertUser(User):
    net_id = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    courses_taken = models.ManyToManyField("Class", related_name="courses")
    interested_classes = models.ManyToManyField("Class", related_name='class_followers')
    current_class_schedule = models.ManyToManyField("Class", related_name='students')
    current_class_schedule_confirmed = models.BooleanField(default=False)
    major = models.ManyToManyField("Major", related_name='students')

    @property
    def has_phone_number(self):
        if self.phone_number is not None and re.match(r'\+\d+', self.phone_number):
            return True
        return False


class Major(models.Model):
    major_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    requirements = models.ManyToManyField("Course", related_name='+')

class Course(models.Model):
    course_id = models.CharField(max_length=30, unique=True)
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    offering = models.BooleanField(default=None)

class Class(models.Model):
    class_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100, blank=True)
    section = models.CharField(max_length=30)
    period = models.CharField(max_length=50)
    parent_course = models.ForeignKey("Course")
    location = models.CharField(max_length=100)
    open = models.BooleanField(default=None)
    format = models.CharField(max_length=20)
    professor = models.CharField(max_length=100)
    time = models.CharField(max_length=100, blank=True)
    rmp_link = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        old_open = self.open
        super(Class, self).save(*args, **kwargs)
        new_open = self.open
        if new_open:
            followers = self.class_followers.all()
            for follower in followers:
                if follower.has_phone_number:
                    send_text_msg(follower.phone_number, "{0} class is now open, remember to sign up :)".format(self.parent_course.course_id))


def send_text_msg(number, text):
    account = "ACaea9723237e5b57f51c51b06e4df47b2"
    token = "bb936a4194d49550d31581c672aff5b8"
    client = TwilioRestClient(account, token)

    message = client.messages.create(
        to=number, 
        from_="+17182853860",
        body=text
    )





