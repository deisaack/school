from django.db import models
from django.conf import settings
from school.klasses.models import Klass

User = settings.AUTH_USER_MODEL


class BaseProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)

    class Meta:
        abstract = True


class Profile(BaseProfile):
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (('MALE', MALE), ('FEMALE', FEMALE))
    gender = models.CharField(max_length=1, default=FEMALE, choices=GENDER_CHOICES)
    def __str__(self):
        return "{}'s profile". format(self.user)


class Parent(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    def __str__(self):
        pass

class Student(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    reg_no = models.CharField(max_length=20, null=True, blank=True)
    parent = models.ForeignKey(Parent, null=True, blank=True)
    klass = models.ForeignKey(Klass, null=True, blank=True)

    def __str__(self):
        return self.reg_no

