from django.contrib import admin

from .models import profile,user_details

from .models import Quizes


admin.site.register(Quizes)



# Register your models here.
admin.site.register(profile)

admin.site.register(user_details)