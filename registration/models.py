from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# For profile which includes photo and username
# class Profile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   image = models.ImageField(default='default.jpg', upload_to='profile_pics')

# def __str__(self):
# return f'{self.user.username} Profile'

# def save(self):
# super().save()

#img = Image.open(self.image.path)

# if img.height > 300 or img.width > 300:
#   output_size = (300, 300)
#   img.thumbnail(output_size)
#   img.save(self.image.path)


class Mentor(models.Model):
    hostel = models.CharField(max_length=20, default=False)
    discp = models.TextField(blank=True)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    year = models.CharField(max_length=20, default="2018")
    degree = models.CharField(max_length=100, default="BTech")
    department = models.CharField(max_length=100, default="Civil")
    maxmentees = models.IntegerField(default=0)
    score = models.FloatField(default=0.0)
    available = models.BooleanField(default=True)
    maxscore = models.FloatField(default=0.0)
    country = models.CharField(max_length=100, default="India")
    interest = models.CharField(max_length=200, null=True)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    password = models.CharField(max_length=20)
    fullname = models.CharField(max_length=100, blank=True)
    rollno = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    contactno = models.CharField(max_length=100, blank=True)
    sop = models.CharField(max_length=500, blank=True)
    suggestions = models.CharField(max_length=500, blank=True)
    pref_1 = models.OneToOneField(
        Mentor, blank=True, null=True, on_delete=models.CASCADE, related_name='pref1')
    pref_2 = models.OneToOneField(
        Mentor, blank=True, null=True, on_delete=models.CASCADE, related_name='pref2')
    pref_3 = models.OneToOneField(
        Mentor, blank=True, null=True, on_delete=models.CASCADE, related_name='pref3')
    pref_4 = models.OneToOneField(
        Mentor, blank=True, null=True, on_delete=models.CASCADE, related_name='pref4')
    pref_5 = models.OneToOneField(
        Mentor, blank=True, null=True, on_delete=models.CASCADE, related_name='pref5')
