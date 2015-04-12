import json
import sys
import os

from django.db.utils import IntegrityError
from basic.models import Major, Course, Class

def import_from_json(file_path):
    f = open(file_path, "r")
    dict = json.loads(f.read())
    f.close()
    try:
        m = Major(major_id=dict["major_id"])
        m.save()
    except IntegrityError:
        pass
    for course in dict["courses"]:
        curr_course = Course(
            course_id=course["course_id"], 
            course_name=course["course_name"], 
            description=course["description"], 
            offering=course["offering"]
        )
        try:
            curr_course.save()
        except IntegrityError:
            pass
        curr_course = Course.objects.get(course_id=curr_course.course_id)
        if course.get("classes") is not None:
            for c in course.get("classes"):
                curr_class = Class(
                    class_id=c["class_id"],
                    format=c["format"],
                    section=c["section"],
                    period=c["period"],
                    location=c["location"],
                    open=c["open"],
                    professor=c["professor"],
                    parent_course = curr_course,
                )
                try:
                    curr_class.save()
                except IntegrityError as e:
                    pass


