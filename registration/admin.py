from django.contrib import admin
from .models import Mentor
from .models import Preference
from .models import Profile
from .models import Information

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Preference)
admin.site.register(Profile)
admin.site.register(Information)
