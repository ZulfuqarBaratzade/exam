from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Login_User)
class LoginUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','password','profile_img','updated_date','created_date']
    search_fields = ['id','username']
    list_editable=['username','profile_img']

    class Meta:
        model = Login_User