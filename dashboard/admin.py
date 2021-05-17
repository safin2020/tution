from django.contrib import admin
from .models import JoiningClass
# Register your models here.
@admin.register(JoiningClass)

class JoinAdmmin(admin.ModelAdmin):
    list_display = [
        'joiningText',
        'classlink',
        'active'
    ]

