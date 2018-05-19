from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = "Course Name has to be longer than 5 characters"
        if len(postData['desc']) < 16:
            errors['desc'] = "Course description should be longer than 15 characters"

        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    def __repr__(self):
        return "<Course Object:{} {}>".format(self.name, self.desc)



