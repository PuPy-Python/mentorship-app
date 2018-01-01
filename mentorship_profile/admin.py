from django.contrib import admin

from .models import Profile, Mentor, Mentee

# Register your models here.
admin.site.register(Profile)
admin.site.register(Mentor)
admin.site.register(Mentee)
