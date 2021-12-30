from django.contrib import admin

from .forms import ProfileForm
from .models import Profile 

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('id','external_id', 'name')
    form = ProfileForm