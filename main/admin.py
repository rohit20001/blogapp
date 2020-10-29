from django.contrib import admin
from main.models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
     list_display = ('title','posted_date')


admin.site.register(Post, PostAdmin)

