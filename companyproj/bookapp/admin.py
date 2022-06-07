from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
 list_display = ('id', 'Book_Name', 'title','author', 'summary','language','total_copies','available_copies')
