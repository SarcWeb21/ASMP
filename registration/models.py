from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages

# Create your models here.


class Mentor(models.Model):
    hostel = models.CharField(max_length=20, default=False)
    discp = models.TextField(blank=True)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    year = models.CharField(max_length=20, default="2018")
    degree = models.CharField(max_length=100, default="BTech")
    city = models.CharField(max_length=100, default="Mumbai")
    department = models.CharField(max_length=100, default="Civil")
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    maxmentees = models.IntegerField(default=0)
    score = models.FloatField(default=0.0)
    available = True
    maxscore = models.FloatField(default=0.0)

    # def maxscore(max_mentees):
    #     if max_mentees == 1:
    #         return 5
    #     elif max_mentees == 2:
    #         return 9
    #     elif max_mentees == 3:
    #         return 12
    #     elif max_mentees == 4:
    #         return 15

    # max_score = maxscore(max_mentees)
    # available = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)
    password = models.CharField(max_length=20)


class Information(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    cpi = models.CharField(max_length=5)
    address = models.CharField(max_length=200)
    department = models.CharField(max_length=50)
    rollno = models.CharField(max_length=12)


class Preference(models.Model):

    preference_no = models.IntegerField(default=0)
    mentor_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
